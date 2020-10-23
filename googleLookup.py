import sys
import requests
import math
import json


def hasNumbers2(String):
    return any(char.isdigit() for char in String)


def sameStreet2(street1, street2):
    list1 = street1.split('&')
    list2 = street2.split('&')
    for item in list1:
        if item in list2:
            return True

    set1 = street1.split(' ')
    set2 = street2.split(' ')
    remove_list = ["Dr", "Drive", "Ave", "Rd", "Road", "PI", "St", "Cir", "Blvd",
                   "NW", "SW", "NE", "SE", "S", "N", "E", "W"]
    for item in remove_list:
        if item in set1:
            set1.remove(item)
        if item in set2:
            set2.remove(item)
    string1 = ""
    string2 = ""
    for item in set1:
        string1 += item + " "
    for item in set2:
        string2 += item + " "
    if string1 == string2:
        return True

    is_same = 0
    for item in set1:
        if item in set2:
            is_same += 1
    if is_same >= 2:
        return True
    return False


def get_address2(df, dataFrame, api_key, index, global_index):
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
    if hasNumbers2(address_list[0]):
        Street = address_list[1]
    else:
        Street = street_w_No
    Street = Street.strip()
    dataFrame.at[global_index, 'Street'] = Street # global
    return Street


def binarySearch2(df, dataFrame, api_key):
    start = df.index[0]
    end = df.index[-1]
    mid = math.ceil((start + end) / 2)

    local_start = 0
    local_end = len(df) - 1
    local_mid = math.ceil((local_start + local_end) / 2)
    # find start point address
    if dataFrame.iloc[start]['Street'] == "":
        start_address = get_address2(df, dataFrame, api_key, local_start, start)
    else:
        start_address = dataFrame.iloc[start]['Street']

    # find mid point address
    if dataFrame.iloc[mid]['Street'] == "":
        mid_address = get_address2(df, dataFrame, api_key, local_mid, mid)
    else:
        mid_address = dataFrame.iloc[mid]['Street']

    # find end point address
    if dataFrame.iloc[end]['Street'] == "":
        end_address = get_address2(df, dataFrame, api_key, local_end, end)
    else:
        end_address = dataFrame.iloc[end]['Street']

    # base case
    if len(df) <= 2 and start_address != end_address:
        return None

    elif (start_address == mid_address and mid_address == end_address) or (
            sameStreet2(start_address, mid_address) and sameStreet2(mid_address, end_address)):

        if local_end - local_start < 2000:  # safe interval can be vary
            return None
        else:
            binarySearch2(df.iloc[local_start:local_mid], dataFrame, api_key)
            binarySearch2(df.iloc[local_mid:], dataFrame, api_key)

    else:
        binarySearch2(df.iloc[local_start:local_mid + 1], dataFrame, api_key)
        binarySearch2(df.iloc[local_mid:], dataFrame, api_key)


def df_cleanup2(df):
    df_len = len(df)
    buffer = df.iloc[0]['Street']
    for i in range(1, df_len):
        if i == df_len - 1:
            break
        if df.iloc[i]['Street'] == buffer or sameStreet2(df.iloc[i]['Street'], buffer) or df.iloc[i]['Street'] == "":
            df.at[i, 'Street'] = ""
        else:
            df.at[i-1, 'Street'] = buffer
            buffer = df.iloc[i]['Street']
    return df


def main(dataFrame, api_key):
    dataFrame["Street"] = ""
    binarySearch2(dataFrame, dataFrame, api_key)   
    df_cleanup2(dataFrame)
    return dataFrame


if __name__ == '__main__':
    api_key = sys.argv[1]
    main(api_key)
