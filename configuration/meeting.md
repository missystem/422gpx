# 422 Group Project 1   

## DUE TIME: OCT 23, 17:00

## Weekly meeting time   
* Monday 4-6pm     
* Friday 5-7pm   

### Wednesday(Oct 21, 2020) Short Meeting:  
* 12pm - 1pm  
* 4pm - 6pm 

---
   
## Meeting Overview:
1. [Monday - Oct 5th](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md#monday---oct-5th)
2. [Wednesday - Oct 7th](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md#wednesday---oct-7th)
3. [Monday - Oct 12th](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md#monday---oct-12th)
4. [Friday - Oct 16th](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md#friday---oct-16th)
5. [Monday - Oct 19th](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md#monday---oct-19th)  
6. [Wednesday - Oct 21st](https://github.com/missystem/422gpx/blob/main/configuration/meeting.md#wednesday---oct-21st)
   
---

### Group role assignments:   
* Missy - Repo Master : Clean repo and make sure things are structured nice
* Lindsay - Build Master / Architect : Overall build plan and design
* Donna - Documentation Boss / Schedule : Make sure everything is on track and document meetings and project
* Xuehai - Quality Assurance : Test code and modules to make sure all is running smoothly
   
---

## Project Overview / Sketch out MVP:  
* [Project description](https://uo-cis422.github.io/chapters/projects/reverse/reverse.html)   
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
    Oct 21st --> Deadline for Missy and Lindsay  
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
  
### Monday - Oct 12th  
* UPDATES: 
  - Donna finished her assignment and will now go around helping people especially in regards to Pandas.
  - Xuehai and Missy have finished the psuedocode and you'retesting the actual code.
  - Lindsay Has algorithms and ideas about the project and will work on them this week.
  - Lindsay spoke with Donna and got an approval for the algorithms! 
* GOALS:
  - Xuehai and Missy have a meeting with Michal and will finish their part by the end of the week.
  - Donna will help everyone with pandas. 
  - Lindsay will work on the project until Wednesday and we'll decide what the next steps are as a team
         
---

### Friday - Oct 16th
  * UPDATES: 
      - Donna's update: Research in HTMl and Using visual maps to show the route to make a more interesting UI. Also started working on the user documentation, but will work on it more when we discuss it in more detail and set clear expectations. 
      - Xuehai and Missy: Main function is down but their debugging now.  
                          Also talk about the user documentation to show progress while the API is fetching things.
      - Lindsay: Third module is done. She demonstrated how it works.   
                 Lindsay and Donna met over the week and decided to keep all data points in the second module, so module two will not be filtering the dataframe.
  * Plan for putting things together:
      - Lindsay showed her ideal input and Missy and Xuehai are arranging their output to look like that. Donna will be "on call" to help with any pandas issues if needed.
      - for the final product the Skeleton.py file is going to be the "main" back end file, which will call upon all other files. 
  * Discuss use casses & plan deployment:
      - If we can finish draft 1 by Tuesday we can try to upgrade. If not we stick with that one.
          - either have an html website that shows the table.
          - or have an html website that lets the user download the csv file.
          - worse case, we make a bash interface.
          - Host website on github.
  *  Goals for next week:
      - Finish street lookup by Monday - Missy & Xuehai
      - Hosting on github (Missy will be the Github Shifu)
      - Lindsay will make a skeleton code that puts things together.
      - Figure out if we need to use Flask - Donna will ask on piazza
      - write html/css and maybe js for website - Lindsay can start on Wednesday afternoon
      
---

### Monday - Oct 19th      
* **UPDATES**:
  - Donna and the logs: Developer log and developer documentation are done (need to talk to module 2 folks about some features)
  - Xuehai and Missy present their work and finished module. Now we focus on "connecting" module 2 to moduel 3.
    - Module 2 must tidy-up the dataframe and street names.
  - Linday has uploaded a placeholder-html file. She mentioned we might not be able to use github to launch the website. 
    - We will have to use flask.
* **PLAN**:
  - Things are needed:
    1. Back-end:
        - Fix module 2 and post on github: **Xuehai**
        - Testing : **Xuehai** (Quality assurance) 
    2. Front-end:
        - Learn Flask and how to use it: **Donna & Missy** 
        - html & css & java script: **Lindsay**
        - Hosting: **Lindsay**
        - Documentation: **Donna**  
        
---

### Wednesday - Oct 21st
* **Checking in**:
   - Missy and Donna: Still working on flask and heroku
   - Xuehai: Testing skeleton and all modules
   - Lindsay: working on html files
   
   
---

### Thursday - Oct 22nd
* **Prep For Submissoin**:
   - Missy and Donna: fixed flask and html
   - Xuehai: Create a new API
   - Lindsay: fix hosting on Heroku
