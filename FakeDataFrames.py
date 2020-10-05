#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime 
import time
import gpxpy
import gpxpy.gpx
import requests

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


DataFrame1 = pd.read_csv('track_points.csv', sep=",", usecols=(0,1))


# In[3]:


DataFrame1.head()


# In[4]:


StreetName = ['Franklin', 'Alder', 'patterson', 'Agate', '13th', '14th', '15th', '16th', 'Olive st', 'Hilyard']


# In[5]:


DataFrame2 = DataFrame1.head(10).copy()


# In[6]:


DataFrame2['Street_Name'] = StreetName


# In[7]:


DataFrame2.head()


# In[ ]:





# In[ ]:





# In[ ]:




