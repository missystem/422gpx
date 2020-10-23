# Documentation for Users:     
   
Welcome! Thank you for using our services!    
This program will take your gpx file and give you a table with turn by turn directions.   
[Click here to our webapp](https://gpx422.herokuapp.com/)
    
### How to use it:
#### 1. Choose an API.   
* In this program you can choose between the Google API and TAMU API.   
* Hint: 
    - Google API is faster and great for large data file, at the expense of accuracy.   
        - It will take roughly 2 and a half minutes to run a GPX file with 10,000 data points
        - Google API key is able to take care of a relatively larger amount of data points
    - TAMU API is limited to 5000 points, but is more accurate. So, it is much better for smaller files.
        - It will take about 7 to 8 minutes to run a GPX file with 10,000 data points
        - TAMU’s address look up is more accurate, but it has fewer attempt times limits
    
#### 2. Get API key:
* **TAMU:**
    * Go to [TAMU Geoservice website](https://geoservices.tamu.edu/UserServices/Profile/Default.aspx) register an account, then follow the steps show in figures
    * Click on **Services** on the top of the page    
    <img width="635.5" height="333" src="https://github.com/missystem/422gpx/blob/main/userImage/1.png"> <br />
    * Click on **Reverse Geocoding** on the left side of the page
    <img width="652.5" height="332.5" src="https://github.com/missystem/422gpx/blob/main/userImage/2.png"> <br />
    * Scroll down a bit and you will see **Start Processing Data** under Reverse Geocoding APIs    
    <img width="652.5" height="453" src="https://github.com/missystem/422gpx/blob/main/userImage/3.png"> <br />
    * Click **REST** in this step   
    <img width="652.5" height="455" src="https://github.com/missystem/422gpx/blob/main/userImage/4.png"> <br />
    * Go to **click here for your API key**       
    <img width="652.5" height="454.5" src="https://github.com/missystem/422gpx/blob/main/userImage/5.png"> <br />
    * Then your API key will show on the page, copy it.        
    <img width="652.5" height="454" src="https://github.com/missystem/422gpx/blob/main/userImage/5.png"> <br />

* **Google:**
    * Sign up for a Google account or log in if you already have one.
    * Go to [Google developer page](https://developers.google.com/maps/documentation/geocoding/get-api-key)
    * Click on **project selector page**       
    <img width="651" height="454.5" src="https://github.com/missystem/422gpx/blob/main/userImage/11.png"> <br />
    * In this page, click on **create project** to create a Google Cloud project     
    <img width="652.5" height="429.5" src="https://github.com/missystem/422gpx/blob/main/userImage/12.png"> <br />
    * Once you finished creating a project, you will see **APIs & Services > Credentials page**, click on that       
    <img width="652.5" height="429" src="https://github.com/missystem/422gpx/blob/main/userImage/13.png"> <br />
    * On the Credentials page, click Create credentials -> API key.     
    <img width="652.5" height="429" src="https://github.com/missystem/422gpx/blob/main/userImage/14.png"> <br />
    * The API key will show on your screen; copy it.      
    <img width="555" height="346" src="https://github.com/missystem/422gpx/blob/main/userImage/15.png"> <br />
           
* Once you copied your API key, return to our web page. 
    

---
   
For developers who want to use or modify our work: [Developer Manual](https://github.com/missystem/422gpx/blob/main/configuration/developer_manual.md)             
--- 

