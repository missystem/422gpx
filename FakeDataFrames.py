#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime 
import time
import gpxpy
import gpxpy.gpx
import requests


def GenDataFrames():

	DataFrame1 = pd.read_csv('track_points.csv', sep=",", usecols=(0,1))
	DataFrame1.head()
	StreetName = ['Franklin', 'Alder', 'patterson', 'Agate', '13th', '14th', '15th', '16th', 'Olive st', 'Hilyard']
	DataFrame2 = DataFrame1.head(10).copy()
	DataFrame2['Street_Name'] = StreetName
	DataFrame2.head()

	return DataFrame2

def main():
	GenDataFrames()
	return 0

if __name__ == "__main__":
	main()
