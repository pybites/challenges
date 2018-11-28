# from datetime import datetime
# from datetime import timedelta

# current time
# now = datetime.today()
# print(str(now))

import os
import time, datetime

duration = 20
timeUnit = 1
timeDuration = datetime.timedelta(seconds = duration)
dt = datetime.timedelta(seconds = timeUnit)

print(f"Pause for {duration} minutes. Hit enter when ready to start the timer.")
input()
for i in range(duration):
    print("\r"+str(timeDuration),end = "")
    timeDuration-=dt
    time.sleep(timeUnit)
print("\r"+str(timeDuration))
os.system("echo 'Time over!\a'")
