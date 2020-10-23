import requests
import math
import json


def get_address(df, dataFrame, api_key, index, global_index):
    df_len = len(df)
    lon = df.iloc[index][0]
    lat = df.iloc[index][1]
    latlng = str(lat) + "," + str(lon)
    web_input = {'latlng': latlng, 'key': str(api_key)}
    website = requests.get('https://maps.googleapis.com/maps/api/geocode/json?',
                           params=web_input)
    json_read = json.loads(website.content)
    street = json_read['results'][0]['formatted_address']
    street_split = street.split(',')
    street_w_No = street_split[0]
    address_list = street_w_No.split(' ', 1)
    if address_list[0].isnumeric():
        Street = address_list[1]
    else:
        Street = street_w_No
    Street = Street.strip()
    dataFrame.at[global_index, 'Street'] = Street # global
    return Street


def binarySearch(df, dataFrame, api_key):
    start = df.index[0]
    end = df.index[-1]
    mid = math.ceil((start + end) / 2)

    local_start = 0
    local_end = len(df) - 1
    local_mid = math.ceil((local_start + local_end) / 2)
    # find start point address
    if dataFrame.iloc[start]['Street'] == "":
        start_address = get_address(df, dataFrame, api_key, local_start, start)
    else:
        start_address = dataFrame.iloc[start]['Street']

    # find mid point address
    if dataFrame.iloc[mid]['Street'] == "":
        mid_address = get_address(df, dataFrame, api_key, local_mid, mid)
    else:
        mid_address = dataFrame.iloc[mid]['Street']

    # find end point address
    if dataFrame.iloc[end]['Street'] == "":
        end_address = get_address(df, dataFrame, api_key, local_end, end)
    else:
        end_address = dataFrame.iloc[end]['Street']

    # base case
    if len(df) <= 2 and start_address != end_address:
        return None

    elif start_address == mid_address and mid_address == end_address:

        if local_end - local_start < 2000:  # safe interval can be vary
            return None
        else:
            binarySearch(df.iloc[local_start:local_mid], dataFrame, api_key)
            binarySearch(df.iloc[local_mid:], dataFrame, api_key)

    else:
        binarySearch(df.iloc[local_start:local_mid + 1], dataFrame, api_key)
        binarySearch(df.iloc[local_mid:], dataFrame, api_key)


def df_cleanup(df):
    df_len = len(df)
    buffer = df.iloc[0]['Street']
    for i in range(1, df_len):
        if i == df_len - 1:
            break
        if df.iloc[i]['Street'] == buffer or df.iloc[i]['Street'] == "":
            df.at[i, 'Street'] = ""
        else:
            df.at[i-1, 'Street'] = buffer
            buffer = df.iloc[i]['Street']
    return df