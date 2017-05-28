# -*- coding: utf-8 -*-
"""
------------------------------------------------------
@author: jhervas

@name: Personal Podcast Assistant

@date: 03/05/2017

@v: 1.0

This script will manage a database with your favourite
podcasts and will update the db with the new ones each
week. Aditionally, it will notify you by email when it
finds new podcasts.
------------------------------------------------------
"""

def packages_import():
    '''Let's start by importing the required packages.'''
    try:
         import feedparser, sqlite3, re, smtplib, schedule, time
         return feedparser, sqlite3, re, smtplib, schedule, time
    except:
         print('''
================================
= INSTALLING REQUIRED PACKAGES =
================================
               ''')
         import pip
         def install(package):
             pip.main(['install', package])
         try:
             requisites = ["feedparser", "sqlite3", "re", "smtplib", "schedule", "time"]
             for package in requisites:
                 install(package)
             import feedparser, sqlite3, re, smtplib, schedule, time
             return feedparser, sqlite3, re, smtplib, schedule, time
         except:
             print('''
================================
===== INSTALLATION FAILURE =====
================================
			''')

def database_connection():
    '''This will manage the connections to the db'''
    try:
        conn = sqlite3.connect('posts.db')
        return conn
    except:
        print('''
================================
=== DATABASE CONNECTION ERROR ==
================================
          ''')

def feedparsing():
    '''Now let's read the feed from our favourite podcast'''
    try:
        feed = feedparser.parse("https://talkpython.fm/episodes/rss")
        return feed
    except:
        print('''
================================
===== FEED LECTURE FAILLURE ====
================================
		''')

def create_database():
    '''If the database dosn't exist, let's create it.'''
    conn = database_connection();
    c = conn.cursor()
    sql = '''
    		create table if not exists 
    		Podcasts (
	    		Title text,
	    		Description text,
	    		Link text,
	    		Played BIT DEFAULT 0
    		);
    		'''
    try:
    	c.execute(sql)
    	conn.commit()
    	print('''
================================
======= DATABASE CREATED =======
================================
		''')
    except:
        print('''
================================
==== ERROR CREATING DATABASE ===
================================
		''')

def update_database():
    '''This is the most important function.'''
    new_podcasts = [] #This variable will help us in the next functions
    feed = feedparsing()
    conn = database_connection();
    c = conn.cursor()
    c.execute('SELECT Title FROM Podcasts')
    for podcast in feed.entries: #Let's check with out db if there are new posts
    	if podcast.title not in c.fetchall():
         new_podcasts.append([podcast.title, podcast.link])
         raw_description = podcast.description
         description = re.sub("<.*?>", "", raw_description)
         description = re.sub('".*?"', "", raw_description)
         sql = '''INSERT INTO Podcasts (Title,Description,Link,Played) VALUES ("'''+podcast.title+'''","'''+description+'''","'''+podcast.link+'''",0);'''
         c.execute(sql)
    conn.commit()
    print('''
================================
======= DATABASE UPDATED =======
================================
	''')
    return new_podcasts


def send_mail(new_podcasts_list):
    '''Now let's going to notify the user that there are new podcasts'''
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    
    #You will need to change this part. Replace the data below with your personal credentials
    #Remember to use your personal gmail account and don't share this data with anyone!!
    smtp_server.login('your_personal_email_here@gmail.com', 'your_app_password_here')
    
    text_body = ""
    for podcast in new_podcasts_list:
        text_body += 'Title: '+podcast[0]+'\nLink: '+podcast[1]+'\n\n'

    smtp_server.sendmail('email_sender@gmail.com', 
                         'email_receiver@gmail.com', 
                         'Subject: New podcasts!\n'+text_body)

    smtp_server.quit()    
    print('''
================================
========== EMAIL SENT ==========
================================
	''')  
    
def main(): 
    '''Finally, let's get it all together.'''
    create_database()
    new_podcasts = update_database()
    send_mail(new_podcasts)
    

'''And let's make it run!'''
if __name__ == "__main__":
    feedparser, sqlite3, re, smtplib, schedule, time = packages_import()   
    schedule.every().wednesday.at("10:52").do(main) #You can change this variable to change the schedule
    while True:
        schedule.run_pending()
        time.sleep(1)
    

