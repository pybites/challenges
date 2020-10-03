#52 - Create your own Pomodoro Timer
from datetime import timedelta, datetime
from os import system

def timer(prompt, duration):
    system('clear')
    end_time = datetime.now() + duration
    while datetime.now() < end_time:
        print(prompt,end_time - datetime.now(),end='\r')
    print

system('clear')
try: 
    duration = timedelta(minutes=int(input('Duration (minutes): (default = 1 minute) ')))
except :
    duration = timedelta(minutes=1)

while True:
    timer('Pomodoro Timer:', duration)
    try:
        break_time = int(input('Break Duration (in minutes or anything else to stop): '))
        timer('Break:', duration)
    except:
        break
    

# Overwrite print 
#https://stackoverflow.com/questions/5419389/how-to-overwrite-the-previous-print-to-stdout-in-python