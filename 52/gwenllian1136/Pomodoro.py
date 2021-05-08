# countdown alarm
# set a time e.g. 20 minutes, counts down and then alarm

from datetime import datetime
from datetime import timedelta
import time

counter_str=input("How many mins to you want to count down ?")
counter=int(counter_str)

if counter<=0:
    counter=1
now_time=datetime.today()
the_gap=timedelta(minutes=counter)
Alarm_time=now_time+the_gap

print('Start time is '+datetime.now().strftime('%H:%M:%S'))
while datetime.now()<Alarm_time:
    time.sleep(1)

print('It''s '+ Alarm_time.strftime('%H:%M:%S')+ '. Please Stop!')
