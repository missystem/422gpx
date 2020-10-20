#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime 
import time
import radix
import gpxpy
import gpxpy.gpx
import requests
import math
import json

get_ipython().run_line_magic('matplotlib', 'inline')


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
            DataFrame2.at[global_index,'streetName'] = "Not Available" # global
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
            DataFrame2.at[global_index,'streetName'] = "Not Available" # global
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
    DataFrame2.at[global_index,'streetName'] = streetName # global
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
    if DataFrame2.iloc[start]['streetName'] == "":
        local_start, start_address = get_address(df, local_start, start, 1)    
    else:
        start_address = DataFrame2.iloc[start]['streetName']
    
    # find mid point address 
    if DataFrame2.iloc[mid]['streetName'] == "":
        local_mid, mid_address = get_address(df, local_mid, mid, 1)
    else:
        mid_address = DataFrame2.iloc[mid]['streetName']
    
    # find end point address 
    if DataFrame2.iloc[end]['streetName'] == "":
        local_end, end_address = get_address(df, local_end, end, 0)
    else:
        end_address = DataFrame2.iloc[end]['streetName']
    
    # base case
    if len(df) <= 2 and start_address != end_address:
        print("<= 2, I'm returning")
        for index, item in df.iterrows():
            row, col, streetAddress = item
            l = [row, col]
            turn_pts.append(l)
        print("turning points:", turn_pts)
        return None
    
    elif start_address == mid_address and mid_address == end_address:
        
        if local_end - local_start < 80:  # 
            print("I'm returning...")
            print("turning points:", turn_pts)
            return None
        else:
            binarySearch(df.iloc[local_start:local_mid])
            binarySearch(df.iloc[local_mid:])
            
    else:
        binarySearch(df.iloc[local_start:local_mid+1])
        binarySearch(df.iloc[local_mid:])


# In[ ]:


def main(DataFrame2):
    DataFrame2["streetName"]=""
    turn_pts = list()
    binarySearch(DataFrame2)
    return DataFrame2

if __name__ == "__main__":
    main()

