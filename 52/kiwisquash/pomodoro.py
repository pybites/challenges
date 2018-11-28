# from datetime import datetime
# from datetime import timedelta

# current time
# now = datetime.today()
# print(str(now))

import os
import time, datetime

duration = 20
timeUnit = 1
timeDuration = datetime.timedelta(minutes = duration)
dt = datetime.timedelta(seconds = timeUnit)

print(f"Pause for {duration} minutes. Hit enter when ready to start the timer.")
input()
for i in range(duration):
    print(timeDuration)
    timeDuration-=dt
    time.sleep(timeUnit)
os.system("echo 'Time over!\a'")
