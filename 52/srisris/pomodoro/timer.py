""" PCC52 - Create your own Pomodoro Timer 
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import datetime, timedelta

now = datetime.now()
interval = timedelta(minutes=1)
end_time = now + interval
print(now)
print(end_time)

stopFlag = False
while stopFlag == False:  
    if datetime.now() >= end_time:
        stopFlag = True
        print("Tring Tring Tring -  Time is up")