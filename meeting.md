# 422 Group

## meeting time   
Monday 4-6pm     
Friday 5-7pm     
https://developers.google.com/maps/documentation/geocoding/start   
   
http://geoservices.tamu.edu   
   
---

### Group role assignments:   
* Missy - Repo Master : Clean repo and make sure things are structured nice
* Lindsay - Build Master / Architect : Overall build plan and design
* Donna - Documentation Boss / Schedule : Make sure everything is on track and document meetings and project
* Xuehai - Quality Assurance : Test code and modules to make sure all is running smoothly
   
---

## Project Overview / Sketch out MVP:  
divide MVP in 3 "chunks", assigned to each person:  

    1. Parse_gpx (pathname to gpx file) -> pandas dataframe
        * opens gpx file, pulls out lat, long, and time from each trkpt, and stores it in a data structure
        * python xml parser, gpxpy?, Beautiful Soup are all potentially helpful tools
        * Assignment: Donna
        * We'll try to use pandas since it can create an efficient dataframe and we can use pandas function to process the data
        * Donna will be the "pandas shifu" as she has had previous exprecience with pandas
            ** I thought the Kong Fu Panda reference was hilarious! :)
            
    2. Filtered_data (pandas dataframe) -> pandas dataframe with only data points immediately before and after each turn, and with street names added
        * uses a clever algorithm to get rid of unneeded data points (Binary search, Granular Search, etc.)
            ** could be approach 1 or 2 from the assignment document
                *** every data point that has the same street as the one before and after it → you can eliminate it!*
            ** or could be something different, e.g. sample every 30 seconds
        * GOAL -> eliminate unnecessary points + add street names!!
        * Assignment : Xuehai & Missy
        
    3. Generate_directions (filtered pandas dataframe) -> csv file
        * generates turn-by-turn directions as a text file
            ** calculates distance between each turn (UTM)
            ** determines if it's a left or right turn (or straight ahead, but the street name changed
            ** writes this information to a csv file
        * Assignment : Lindsay
        * the most challenging part, other people join in after finish their own parts
        
    
---
  
### Monday - Oct 5th  
  Rough Timeline:  
    Oct 12th --> Deadline for Donna and Xuehai  
    Ocr 21st --> Deadline for Missy and Lindsay  
   * Parallel: Xuehai should test the code in parallel as the Quality Assurance person.  
    We'll test our individual sections in Jupyter notebook and commit the python executable for that to Github to have in our records.  
    Each member went trhough their progress/struggles about their part so far and cleared up any confusion.    
  
---
  
### Wednesday - Oct 7th  
   * Meeting with Prof.Young and talked about the overall structure of the project and clarified some details. 
   * At each step, each module will be a python executable (.py) file and there will be a main file that will connect all 3 modules and run the program
   * Module 3 doesn't seem to be as challenging as we thought, so Missy's role is switched to a person that jumps from topics to help members who are struggling.
        * She will currently work on Module 4 with Xuehai.
   * Friday meeting is canceled (unless we need to meet)
  
---
  
### Moday - Oct 12th  
* UPDATES: 
  - Donna finished her assignment and will now go around helping people especially in regards to Pandas.
  - Xuehai and Missy have finished the psuedocode and you'retesting the actual code.
  - Lindsay Has algorithms and ideas about the project and will work on them this week.
  - Lindsay spoke with Donna and got an approval for the algorithms! 
* GOALS:
  - Xuehai and Missy have a meeting with Michal and will finish their part by the end of the week.
  - Donna will help everyone with pandas. 
  - Lindsay will work on the project until Wednesday and we'll decide what the next steps are as a team
         
