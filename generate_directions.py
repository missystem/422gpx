#!/usr/bin/env python3

import pandas
from geopy import distance  # for distance calculation
from GpxParser import GpxParse
import datetime
import time
import gpxpy
import requests
import math
import numpy as np  # for bearings calculation


def generate_directions(dataframe):

    # figure cumulative distance for each point

    num_points = len(dataframe["Longitude"])  # helpful variable for loops etc.
    # cumulative distance at start is 0
    # kludge to make a Distance instance of 0
    cumul_distance = [0.0]
    for datapoint in range(1, num_points):
        cumul_distance.append(distance.distance((dataframe["Latitude"][datapoint], dataframe["Longitude"][datapoint]), (
            dataframe["Latitude"][datapoint-1], dataframe["Longitude"][datapoint-1])).miles)
        cumul_distance[datapoint] += cumul_distance[datapoint-1]

    dataframe["Distance"] = cumul_distance

    # temporary kludge to add street names for module develoment, specific to morning_ride.gpx
    hardcode = ["Hayes", "", "", "", "", "", "", "", "", "", "", "Hayes", "18th", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "18th", "Chambers", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Chambers", "14th", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "14th", "Tyler", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Tyler", "5th", "", "", "", "", "", "", "", "", "", "5th", "Blair", "", "", "Blair"]
    dataframe["Street"] = hardcode
    print(dataframe)

    # calculate direction of turn
    turn = [""]*num_points
    # at least .006 miles (~10m) before turn, magic number
    turn_interval = .006
    straight = 20  # if < this many degrees, considered straight
    # outer loop to detect a turn
    for point in range(1, num_points-1):
        if dataframe["Street"][point] != "":  # if it's a point next to a turn
            # pull this calculation out of the while loops
            point_distance = dataframe["Distance"][point]

            if dataframe["Street"][point+1] != "":  # if it's the beginning of a turn
                print("precedes turn", dataframe["Street"][point], point)
                # find the datapoint just over 10m behind
                trace = point - 1  # trace will represent a nearby datapoint for making vectors
                while (point_distance - dataframe["Distance"][trace]) < turn_interval:
                    trace -= 1
                # trace is the index of the fartherst point prior to turn <10m
                # get a bearing for the pre-turn direction
                pre_vector = get_bearing(dataframe["Latitude"][point], dataframe["Longitude"]
                                         [point], dataframe["Latitude"][trace], dataframe["Longitude"][trace])
                print(pre_vector)

            else:  # if it's the first point after a turn
                print("follows turn", dataframe["Street"][point], point)
                trace = point+1
                while (trace < num_points) and ((dataframe["Distance"][trace] - point_distance) < turn_interval):
                    trace += 1
                # get a bearing for the post-turn direction
                # trace and point are reversed from above because direction is outward, not inward
                # and if I have that backwards, I don't think it matters as far as left and right go
                post_vector = get_bearing(dataframe["Latitude"][trace], dataframe["Longitude"]
                                          [trace], dataframe["Latitude"][point], dataframe["Longitude"][point])
                print(post_vector)

                # now use the 2 vectors to figure the turn direction
                bearing_diff = pre_vector - post_vector
                if abs(bearing_diff) < straight:
                    direction = "straight"
                elif bearing_diff < 0:
                    direction = "right"  # this is a guess for now
                else:
                    direction = "left"
                print(direction)

    # compose string with directions for each turn

    # write to CSV file from dictionary


def get_bearing(lat1, lon1, lat2, lon2):
    """
    I got this code from Alex Wien on StackOverflow: https://stackoverflow.com/questions/17624310/geopy-calculating-gps-heading-bearing

    """
    dLon = lon2 - lon1
    y = math.sin(dLon) * math.cos(lat2)
    x = math.cos(lat1)*math.sin(lat2) - math.sin(lat1) * \
        math.cos(lat2)*math.cos(dLon)
    brng = np.rad2deg(math.atan2(y, x))
    if brng < 0:
        brng += 360
    return brng


def main():
    dataFrame = GpxParse("Morning_Ride.gpx")
    generate_directions(dataFrame)


if __name__ == "__main__":
    main()
