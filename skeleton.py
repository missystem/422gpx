#!/usr/bin/env python3
import pandas  # for, like, everything!
from geopy import distance  # for distance calculation
from GpxParser import GpxParse
from generate_directions import generate_directions
from addressLookup import *
import datetime
import time
import gpxpy
import requests
import math  # for bearings calculation
import numpy as np  # for bearings calculation


def main(api_key):
    # start with a gpx we want to generate directions from
    # extract lat and long
    # return a pandas DataFrame
    dataFrame = GpxParse("Morning_Ride.gpx")
    # add an empty street name column
    dataFrame["streetName"] = ""
    # re-set the dataFrame's index
    # binary search highly rely on correct index
    dataFrame = dataFrame.reset_index(drop=True)
    # lookup street name for each data point
    lookedup = binarySearch(dataFrame, api_key)
    # for a contiguous series of data points with the same street, eliminate all but the first and last
    # return the revised pandas DataFrame
    filtered = df_cleanup(lookedup)

    # figure cumulative distance from turn to turn
    # determine direction of turn (left or right)
    # compose string like "make a right turn onto Franklin Blvd."
    # write instructions to CSV
    cue_sheet = generate_directions(filtered)

    return cue_sheet


if __name__ == '__main__':
    main()
