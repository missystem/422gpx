#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import datetime 
import time
import gpxpy
import requests


# In[28]:


def GpxParse(gpx_filename: str):
    ''' 
    Input: Gpx file name
    This parser will create a pandas dataframe consisting of longitude and latitude
    Output: Pandas Dataframe
    '''
    gpx_file = open(gpx_filename, 'r')
    gpx = gpxpy.parse(gpx_file)
    
    #print("{} track(s)".format(len(gpx.tracks)))
    track = gpx.tracks[0]
    
    #print("{} segment(s)".format(len(track.segments)))
    segment = track.segments[0]

    #print("{} point(s)".format(len(segment.points)))
    
    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude,
                 point.elevation, point.time, segment.get_speed(point_idx)])
    

    columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    df = pd.DataFrame(data, columns=columns)
    df = df.drop(['Altitude', 'Time', 'Speed'], axis = 1S)
    #df.head()
    return df


# In[29]:


def main():
    name = "09_27_20.gpx"
    dataframe = GpxParse(name)
    #dataframe.head()
    


# In[30]:


if __name__ == "__main__":
	main()




