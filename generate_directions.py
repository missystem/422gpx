#!/usr/bin/env python3

import pandas
from geopy import distance
from GpxParser import GpxParse
from FakeDataFrames import GenDataFrames
import datetime
import time
import gpxpy
import requests


def generate_directions(dataframe):
    print(dataframe["Longitude"][3], dataframe["Latitude"][3])

    # dataframe.apply(lambda r: distance.distance(
    #     ["Latitude", "Longitude"]), axis=1)
    # print(dataframe)

    # cumulative distance at start is 0
    # kludge to make a Distance instance of 0
    cumul_distance = [distance.distance((44, -123), (44, -123))]
    for datapoint in range(1, len(dataframe["Longitude"])):
        cumul_distance.append(distance.distance((dataframe["Latitude"][datapoint], dataframe["Longitude"][datapoint]), (
            dataframe["Latitude"][datapoint-1], dataframe["Longitude"][datapoint-1])))
        cumul_distance[datapoint] += cumul_distance[datapoint-1]

    dataframe["Distance"] = cumul_distance

    hardcode = ["Hayes", "", "", "", "", "", "", "", "", "", "", "Hayes", "18th", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "18th", "Chambers", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Chambers", "14th", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "14th", "Tyler", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Tyler", "5th", "", "", "", "", "", "", "", "", "", "5th", "Blair", "", "", "Blair"]
    dataframe["Street"] = hardcode
    print(dataframe)

    # calculate direction of turn

    # compose string with directions for each turn

    # write to CSV file from dictionary


def main():
    dataFrame = GpxParse("Morning_Ride.gpx")
    print(dataFrame)
    generate_directions(dataFrame)


if __name__ == "__main__":
    main()
