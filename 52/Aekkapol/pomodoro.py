""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""
import os
from datetime import date
from datetime import datetime
from datetime import timedelta

time_now = datetime.now()
time_now

time_interval = timedelta(minutes=20)

time_end = time_now + time_interval
time_end


print("Start: " + str(time_now))
print("Stop: " + str(time_end))

stop = False
while stop == False:
    time_now_display = str(datetime.now().time())
    # print(time_now_display)
    time_now = datetime.now()
    if time_now >= time_end:
        stop = True
        print("Time is up")
