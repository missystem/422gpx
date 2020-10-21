#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import math
import json



# In[2]:


def get_address(df, index, global_index, one_or_zero):
    df_len = len(df)
    for i in range(df_len):
        print(df.index[i])
    print()
    lon = df.iloc[index][0]
    lat = df.iloc[index][1]
    web_input = {'lon':str(lon), 
                  'lat':str(lat), 
                  'state':"or", 
                  'apikey':"68971949e5f24edba97fb29083c1a604", 
                 'format':"json",
                 'notStore':"false",
                 'version':"4.10"}
    website = requests.get('https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?',
                           params=web_input)
    json_read = json.loads(website.content)
    idx_cp = index
    if one_or_zero == 1:
        while json_read['QueryStatusCode'] != "Success":
            dataFrame.at[global_index,'streetName'] = "Not Available" # global
            global_index += 1
            idx_cp = idx_cp + 1
            lon = df.iloc[idx_cp][0]
            lat = df.iloc[idx_cp][1]
            web_input = {'lon':str(lon), 
                      'lat':str(lat), 
                      'state':"or", 
                      'apikey':"68971949e5f24edba97fb29083c1a604", 
                     'format':"json",
                     'notStore':"false",
                     'version':"4.10"}
            website = requests.get('https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?',
                                   params=web_input)
            json_read = json.loads(website.content)
    else:
        while json_read['QueryStatusCode'] != "Success":
            dataFrame.at[global_index,'streetName'] = "Not Available" # global
            global_index -= 1
            idx_cp = idx_cp - 1 
            lon = df.iloc[idx_cp][0]
            lat = df.iloc[idx_cp][1]
            web_input = {'lon':str(lon), 
                      'lat':str(lat), 
                      'state':"or", 
                      'apikey':"68971949e5f24edba97fb29083c1a604", 
                     'format':"json",
                     'notStore':"false",
                     'version':"4.10"}
            website = requests.get('https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?',
                                   params=web_input)
            json_read = json.loads(website.content)
    address = str(json_read['StreetAddresses'][0]['StreetAddress'])
    address_list = address.split(' ', 1) 
    streetName = address_list[1]
    streetName = streetName.strip()
    dataFrame.at[global_index,'streetName'] = streetName # global
    return idx_cp, streetName


# In[3]:



def binarySearch(df):
    start = df.index[0]
    end = df.index[-1]
    mid = math.ceil((start + end) / 2)
    
    local_start = 0
    local_end = len(df) - 1
    local_mid = math.ceil((local_start + local_end) / 2)
    # find start point address
    if dataFrame.iloc[start]['streetName'] == "":
        local_start, start_address = get_address(df, local_start, start, 1)    
    else:
        start_address = dataFrame.iloc[start]['streetName']
    
    # find mid point address 
    if dataFrame.iloc[mid]['streetName'] == "":
        local_mid, mid_address = get_address(df, local_mid, mid, 1)
    else:
        mid_address = dataFrame.iloc[mid]['streetName']
    
    # find end point address 
    if dataFrame.iloc[end]['streetName'] == "":
        local_end, end_address = get_address(df, local_end, end, 0)
    else:
        end_address = dataFrame.iloc[end]['streetName']
    
    # base case
    if len(df) <= 2 and start_address != end_address:
        # for index, item in df.iterrows():
        #     row, col, streetAddress = item
        #     l = [row, col]
        #     turn_pts.append(l)
        return None
    
    elif start_address == mid_address and mid_address == end_address:
        
        if local_end - local_start < 80:  # safe interval can be vary
            return None
        else:
            binarySearch(df.iloc[local_start:local_mid])
            binarySearch(df.iloc[local_mid:])
            
    else:
        binarySearch(df.iloc[local_start:local_mid+1])
        binarySearch(df.iloc[local_mid:])


# In[4]:


def df_cleanup(df):
    df_len = len(df)
    buffer = df.iloc[0]['streetName']
    for i in range(1, df_len):
        if i == df_len - 1:
            break
        if df.iloc[i]['streetName'] == buffer and df.iloc[i+1]['streetName'] != "" and df.iloc[i+1]['streetName'] != buffer:
            buffer2 = df.iloc[i+1]['streetName']
        elif df.iloc[i]['streetName'] != buffer and df.iloc[i]['streetName'] != "":
            buffer = buffer2
        else:
            df.at[i, 'streetName'] = ""
    return df


# In[ ]:


def main(dataFrame):
    dataFrame["streetName"]=""
    # turn_pts = list()
    binarySearch(dataFrame)
    df_cleanup(dataFrame)
    return dataFrame

if __name__ == "__main__":
    main()

