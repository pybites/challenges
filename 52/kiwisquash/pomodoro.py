# from datetime import datetime
# from datetime import timedelta

# current time
# now = datetime.today()
# print(str(now))

import os, sys
import time, datetime

os.system("clear")

def alert(n=1):
    for _ in range(n):
        os.system("echo '\a'")

def parameters():
    duration = 20
    nLoops = 1
    breakTime = 5
    if len(sys.argv) > 1:
        duration = float (sys.argv[1])
    if len(sys.argv) > 2:
        nLoops = float (sys.argv[2])
    if len(sys.argv)>3:
        breakTime = float (sys.argv[3])
    return duration, nLoops, breakTime

def countDown(timeAmount,timeUnit = 1):
    timeDuration = datetime.timedelta(minutes = timeAmount)
    dt = datetime.timedelta(seconds = timeUnit)
    for i in range(int(60*timeAmount)):
        print("\r"+str(timeDuration),end = "")
        timeDuration-=dt
        time.sleep(timeUnit)
    print("\r"+str(timeDuration))

duration, nLoops, breakTime = parameters() 

print(f"Hit enter when ready to start the timer.")
input()
alert()
print(f"\rStart working! Keep at it for {duration} minutes!")
while nLoops > 0:
    countDown(duration)
    if nLoops > 1:
        alert()
        print(f"\rTime for a {breakTime} minute break!")
        countDown(breakTime)
        alert()
        print(f"\rResume work for {duration} minutes.")
    nLoops-=1
alert(3)
print("Time over!")
