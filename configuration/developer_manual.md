# Documentation for Developers:

**Summary of project**:
    Hikers, runners, and cyclists often record their activities using a phone, fitness watch, or dedicated GPS device. They may upload data from their devices to a system like Strava, MapMyRun, or RideWithGPS, which typically provide analysis, map display, and optional social media sharing.
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
* Output -> a list of turn by turn directions
* Process:
    - We divded the MVP in 3 "chunks", and assigend each module to one person (except for module 2, which was assigned to two people):
        1. Parse_gpx (pathname to gpx file) -> pandas dataframe
            - opens gpx file, pulls out lat, long, and time from each trkpt, and stores it in a data structure
            - gpxpy and pandas are the main libraries used in this module.
        2. Filtered_data (pandas dataframe) -> pandas dataframe with only data points immediately before and after each turn, and with street names added
            - lookup addresses of start, mid, and end data points. If they are not in the same street, then chop the data into two, which are from start->mid, and mid->end. Do the same approach repeatedly until they are on the same street. (binary search)
            - choose a reverse geocoing service (web service) to do the address lookup job.
        3. Generate_directions (filtered pandas dataframe) -> csv file
            - generates turn-by-turn directions as a text file
                - calculates distance between each turn (UTM)
                    - The library had a distance function which was applied to the data frame.
                - determines if it's a left or right turn (or straight ahead, but the street name changed
                    - This was done by finding the angles between two points, if the angle was more than 20 Degrees it was classified as a turn.
                - writes this information to a csv file
<<<<<<< HEAD:configuration/developer_manual.md
    - As for the remaining steps, we have the user interface.   
    ** EXPLAIN USER INTERFACE **
               
=======
    - As for the remaining steps, we have the user interface, which is explained in detail above.
               
                

   
---

>>>>>>> 5bfed539dff58090e342f46394d832a92a6e2083:configuration/documentation.md
