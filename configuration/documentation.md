## [meeting information](https://github.com/missystem/422gpx/blob/main/meeting.md)

### Documentation  
  
1. [Documentation for User]()
2. [Documentation for Developer](https://github.com/missystem/422gpx#documentation-for-developers)
   
---
   
## Documentation for Developers:

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
    - As for the remaining steps, we have the user interface.   
    ** EXPLAIN USER INTERFACE **
               
                

   
---

## Documentation for Users:     

Welcome! Thank you for using our services!    
This program will take your gpx file and give you a table with turn by turn directions.   
[Click here to our webapp](https://gpx422.herokuapp.com/)
    
How to use it:
1. Choose an API.   
* In this program you can choose between the Google API and TAMU API.   
* Hint: 
    - Google API is faster and great for bigger files, at the expense of accuracy.   
    - TAMU API is limited to 5000 points, but is more accurate. So, it is much better for smaller files.
2. Get API key:
* TAMU:
    1. Go to [TAMU Geoservice website](https://geoservices.tamu.edu/UserServices/Profile/Default.aspx) register an account, then follow the steps show in figures
    2. Click on **Services** on the top of the page    
    <img width="635.5" height="333" src="https://github.com/missystem/422gpx/blob/main/userImage/1.png"> <br />
    3. Click on **Reverse Geocoding** on the left side of the page
    <img width="652.5" height="332.5" src="https://github.com/missystem/422gpx/blob/main/userImage/2.png"> <br />
    4. <img width="652.5" height="453" src="https://github.com/missystem/422gpx/blob/main/userImage/3.png"> <br />
    5. <img width="652.5" height="455" src="https://github.com/missystem/422gpx/blob/main/userImage/4.png"> <br />
    6. <img width="652.5" height="454.5" src="https://github.com/missystem/422gpx/blob/main/userImage/5.png"> <br />

* Google:
    a. (Xuehai, idk how to do it)
                
3. Once you have your key, go to our website. 
4. ...
            






