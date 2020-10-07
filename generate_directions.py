#!/usr/bin/env python3

# import pandas
from geopy import distance


def generate_directions(frame: list) -> str:

    # testing ability to read from DataFrame object

    # first convert lat and long into UTM coordinates
    # may not be necessary with geopy

    # calculate distance between turns
    # rough calculate: from post-turn to pre-turn

    point1 = (frame[0]["lat"], frame[1]["long"])
    point2 = (frame[2]["lat"], frame[3]["long"])
    point3 = (frame[4]["lat"], frame[5]["long"])
    print("Hayes: ", point1, " 18th: ", point2, " Chambers: ", point3)
    distance1 = distance.distance(point1, point2)
    distance2 = distance.distance(point2, point3)
    print("distance1: ", distance1, "distance2: ", distance2)

    # first average between before and after coordinates for a turn coordinate
    # figure distance in km from one turn coordinate to the next
    # write to dictionary

    # calculate direction of turn

    # compose string with directions for each turn

    # write to CSV file from dictionary


def make_data():

    mockDict1 = {"index": 1, "lat": 43.0891310, "long": -
                 122.1118960, "time": "17:15:31", "street": "Hayes"}
    mockDict2 = {"index": 2, "lat": 43.0889390, "long": -
                 122.1162580, "time": "17:16:29", "street": "Hayes"}
    mockDict3 = {"index": 3, "lat": 43.0885860, "long": -
                 122.1165880, "time": "17:16:35", "street": "18th"}
    mockDict4 = {"index": 4, "lat": 43.0780780, "long": -
                 122.1179230, "time": "17:19:15", "street": "18th"}
    mockDict5 = {"index": 5, "lat": 43.0778710, "long": -
                 122.1179050, "time": "17:19:20", "street": "Chambers"}
    mockDict6 = {"index": 6, "lat": 43.0747080, "long": -
                 122.1184860, "time": "17:21:04", "street": "Chambers"}
    mockArr = [mockDict1, mockDict2, mockDict3,
               mockDict4, mockDict5, mockDict6]

    print("mockDict4['lat']: ", mockDict4["lat"])
    print("mockArr[4]['lat']", mockArr[4]["lat"])

    return mockArr


def main():
    # dataFrame = FakeDataFrames()
    dataPoints = make_data()
    generate_directions(dataPoints)


if __name__ == "__main__":
    main()
