# from datetime import datetime
# from datetime import timedelta

# current time
# now = datetime.today()
# print(str(now))

import time

duration = 5
timeUnit = 1
unit = "seconds"

print("Pause for {} {}.".format(duration,unit))
for i in range(duration):
    print(i)
    time.sleep(timeUnit)
print("Time over!")
