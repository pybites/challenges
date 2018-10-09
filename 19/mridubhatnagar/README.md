# Event_Fetcher


**FEATURES**
1. Fetches the next Birthday Event from the Calendar.
2. Creates an new event in the Calendar.
3. Email Notification 5 minutes before the event.

**API USED**
Google Calendar API

**ASSUMPTIONS**

1. It is assumed that primary calendar only contains the Birthday Events. Hence, would fetch the next Birthday Event. 

    Alternate approach could be to create a new calendar. Which is only a Birthday Calendar. Get calendar ID for this
    calendar and replace calendarId = 'primary' with the new calendar ID and proceed.
    
2. Python version 3.5.2 is used. Compatible for any version greater than Python3.


**STEPS TO RUN THE CODE**

1. git clone https://github.com/mridubhatnagar/Event_Fetcher.git
2. `cd Event_Fetcher`
3. Enable the Google Calendar API https://developers.google.com/calendar/quickstart/python
4. Go to above link. Click on enable the calendar API.
5. Create or Select from your existing projects. Click on Next. Select download client configrations. 
6. Credentials.json would be downloaded onto your system. Copy from downloads folder and place credentials.json
   the cloned repository.
7. Go into the cloned repository. Create virtual enviornment.
   On Linux
   
   `virutalenv venv`
   
8. Activate the virtual enviornment

   `source venv/bin/activate`
   
9. Install all the requirements.

   `pip install -r requirements.txt`

10. Run the file. 

   `python credentails.py`

11. It will prompt you and token.json would be installed. Once you give the
   allow the application to access the calendar.

**INFORMATION**

1. credentials.py - Is the main source code 
2. config.py - Contains the JSON which is needed for the event creation.


**NOTE**
Enter the url in the browser which gets generated on running the code. To see event created.


