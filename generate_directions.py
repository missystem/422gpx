#!/usr/bin/env python3

import pandas  # for, like, everything!
from geopy import distance  # for distance calculation
from GpxParser import GpxParse
import datetime
import time
import gpxpy
import requests
import math  # for bearings calculation
import numpy as np  # for bearings calculation


def generate_directions(dataframe):
    """Generates a CSV file that serves as a cue sheet

    Args:
        dataframe is a pandas DataFrame 
        Each datapoint (row) has latitude and longitude, plus street name for the point immediately before and immediately after a turn (street change)

    Returns:
        my_cue_sheet.csv has columns for turn (start, right, left, straight, end), cumulative distance from start, and turn-by-turn directions

    Todo: remove lines 37-40, hardcoded street names for sample dataframe
    """

    num_points = len(dataframe["Longitude"])  # helpful variable for loops etc.

    # figure cumulative distance for each point
    cumul_distance = [0.0]  # starting distance is 0
    for datapoint in range(1, num_points):
        cumul_distance.append(distance.distance((dataframe["Latitude"][datapoint], dataframe["Longitude"][datapoint]), (
            dataframe["Latitude"][datapoint-1], dataframe["Longitude"][datapoint-1])).miles)
        cumul_distance[datapoint] += cumul_distance[datapoint-1]
    dataframe["Distance"] = cumul_distance

    # temporary kludge to add street names for module develoment, specific to morning_ride.gpx
    hardcode = ["Hayes", "", "", "", "", "", "", "", "", "", "", "Hayes", "18th", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "18th", "Chambers", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Chambers", "14th", "", "", "", "", "", "", "", "", "", "", "",
                "", "", "14th", "Tyler", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Tyler", "5th", "", "", "", "", "", "", "", "", "", "5th", "Blair", "", "", "Blair"]
    dataframe["Street"] = hardcode

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
                # print("precedes turn", dataframe["Street"][point], point)
                # find the datapoint just over 10m behind
                trace = point - 1  # trace will represent a nearby datapoint for making vectors
                while (point_distance - dataframe["Distance"][trace]) < turn_interval:
                    trace -= 1
                # trace is the index of the fartherst point prior to turn <10m
                # get a bearing for the pre-turn direction
                pre_vector = get_bearing(dataframe["Latitude"][point], dataframe["Longitude"]
                                         [point], dataframe["Latitude"][trace], dataframe["Longitude"][trace])

            else:  # if it's the first point after a turn
                # print("follows turn", dataframe["Street"][point], point)
                trace = point+1
                while (trace < num_points) and ((dataframe["Distance"][trace] - point_distance) < turn_interval):
                    trace += 1
                # get a bearing for the post-turn direction
                # trace and point are reversed from above because direction is outward, not inward
                post_vector = get_bearing(dataframe["Latitude"][trace], dataframe["Longitude"]
                                          [trace], dataframe["Latitude"][point], dataframe["Longitude"][point])

                # now use the 2 vectors to figure the turn direction
                bearing_diff = pre_vector - post_vector
                if abs(bearing_diff) < straight:
                    direction = "straight"
                elif bearing_diff < 0:
                    direction = "right"  # got it right on first guess
                else:
                    direction = "left"
                turn[point-1] = direction

    turn[0] = "start"
    turn[num_points-1] = "end"
    dataframe["Turn"] = turn

    # remove unneeded columns from dataframe
    dataframe = dataframe.drop(["Longitude", "Latitude"], axis=1).copy()
    # remove unneeded rows from dataframe
    dataframe = dataframe[dataframe.Street != ""].copy()
    dataframe = dataframe[dataframe.Turn != ""].copy()
    dataframe.Street = dataframe.Street.shift(-1)
    dataframe = dataframe.reset_index(drop=True)

    #  compose string with directions for each turn
    length = len(dataframe["Street"])
    notes = [""] * length
    for note in range(length):
        turn = dataframe["Turn"][note]
        street = dataframe["Street"][note]
        if turn == "start":
            notes[note] = "Start on " + street
        elif turn == "left":
            notes[note] = "Turn left onto " + street
        elif turn == "right":
            notes[note] = "Turn right onto " + street
        elif turn == "straight":
            notes[note] = "Continue straight onto " + street
        else:
            notes[note] = "End"
    dataframe["Notes"] = notes
    dataframe = dataframe.drop(["Street"], axis=1).copy()

    cue_sheet = dataframe.to_csv("my_cue_sheet.csv")
    return cue_sheet


def get_bearing(lat1, lon1, lat2, lon2):
    """
    I got this code from Alex Wien on StackOverflow: https://stackoverflow.com/questions/17624310/geopy-calculating-gps-heading-bearing
    It takes in the coordinates for two points and determines the bearing of a vector from one point to the other
    brng is the number of degrees clockwise from north
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
    cue_sheet = generate_directions(dataFrame)


if __name__ == "__main__":
    main()
