# Documentation for Developers:

**Summary of project**:
    Hikers, runners, and cyclists often record their activities using a phone, fitness watch, or dedicated GPS device. They may upload data from their devices to a system like Strava, MapMyRun, or RideWithGPS, which typically provides analysis, map display, and optional social media sharing.
    Existing services like Strava provide a variety of analyses and record keeping, but they typically do not provide a fully automated way to extract turn-by-turn directions from a recorded activity. For hikers and runners and some cyclists who travel off-road, this might be very difficult … there may be no suitable database from which to extract suitable cues. For road cyclists, however, it should be possible to extract turn-by-turn directions (a “cue sheet”) from a recording.
    That is what our system will do. The input will be a record consisting of a sequence of (latitude, longitude) pairs, possibly with other information. The output should be a list of turn-by-turn directions, e.g.,
        0.0 km Start at 19th and Agate
        1.2km Left on Franklin Blvd
        1.4km Left on 11th Ave
    
**Background Information**:
* Geocoding:
    - Geocoding means translating place names or descriptions into geographic coordinates, usually latitude and longitude.
* Reverse Geocoding:
    - Geocoding translates addresses into coordinates. Reverse geocoding, as you might guess, translates coordinates to addresses.

* Web Services:
    - A web application (or “web app”) is designed for use by humans. A web service is designed for use by programs. Often it will be called a “web api” or just “api” (application program interface). Sometimes it will be called a REST API or REST service. REST stands for “representational state transfer”, and describes an architectural style for web services and web applications.

**Description**:
* Input -> GPX file
* Output -> a list of turn by turn directions, displayed in table form in an html document
* Process:
    - We divded the minimum viable product (MVP) into 3 "chunks", and assigned each module to one person (except for module 2, which was assigned to two people):
        1. Parse_gpx (pathname to gpx file) -> pandas dataframe
            - opens gpx file, pulls out lat, long, and time from each trkpt, and stores it in a data structure
            - gpxpy and pandas are the main libraries used in this module.
        2. Filtered_data (pandas dataframe) -> pandas dataframe with only data points immediately before and after each turn, and with street names added
            - lookup addresses of start, mid, and end data points. If they are not in the same street, then chop the data into two, which are from start->mid, and mid->end. Do the same approach repeatedly until they are on the same street. (binary search)
            - choose a reverse geocoing service (web service) to do the address lookup job. We offer the user a choice of services, either TAMU (Texas A&M GeoServices) or Google.
        3. Generate_directions (filtered pandas dataframe) -> pandas dataframe with cumulative distance, turn direction, and prose directions added (and extra datapoints removed)
                - calculates cumulative distance from start to each datpoint
                    - The geopy library had a distance function which was applied to the data frame
                - determines if it's a left or right turn (or straight ahead, but the street name changed)
                    - First, find a point a certain distance (currently 20m) back from the point immediately before the turn or ahead of the point immediately after the turn. Use these points to create a vector
                    - Next, use trigonometry to determine the bearing of each vector
                    - Finally, use the bearings before and after each turn to determine turn direction; currently an angle of less than 20 degrees is considered straight
                - composes a prose description of each turn, e.g. "Turn right onto 18th"
                - returns a dataframe with cumulative distance, turn direction, and prose directions for each turn point
    - As for the remaining steps, we have the user interface, which is explained in detail in the user document. We used flask and html and hosted the website on heroku.
    
    - FUTURE FEATURES:
        - In graph.py in the main branch there is some starter code that generates a map of the points. We could develop that further using mplleaflet to show it on an actual map. 
        - We can also add a figure for the altitude over time quite easily using plot and the dataframe.
        - Currently, our address lookup generates some inaccurate addresses; sometimes this is because it picks up addresses on cross streets as the rider continues straight, and sometimes this is because a large area before and after a turn may all be indexed to a single address, as in the case of large box stores on a corner. In the future we may try a modified approach to our binary search lookup algorithm, or another algorithm altogether, to get more accurate results.
        - We hope to remove the requirement that a user obtain his/her own API to enter on our website. Although the process is fairly painless, our tool will be easier for technologically naive people to use if they can skip this step.
         
---

For detailed timeline of our changes, go to our [meeting](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md)                
   
---
