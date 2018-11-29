# from datetime import datetime
# from datetime import timedelta

# current time
# now = datetime.today()
# print(str(now))

import os, sys
import time, datetime

os.system("clear")
def alert():
    os.system("echo '\a'")

def parameters():
    if len(sys.argv) == 1:
        duration = 20
    else:
        duration = float (sys.argv[1])
        if len(sys.argv) == 2:
            nLoops = 1
        else:
            nLoops = float (sys.argv[2])
            if len(sys.argv)>3:
                breakTime = float (sys.argv[3])
            else:
                breakTime = 5
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

print(f"Pause for {duration} minutes. Hit enter when ready to start the timer.")
input()
while nLoops > 0:
    countDown(duration)
    if nLoops > 1:
        print(f"\rTime for a {breakTime} minute break!")
        countDown(breakTime)
        print(f"\rResume work for {duration} minutes.")
    nLoops-=1
print("Time over!")
alert()
