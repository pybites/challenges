from datetime import datetime, timedelta
import time 
import subprocess as sp
import sys

POMODORO_TIMER_MINUTES = sys.argv[1]
if int(sys.argv[1]) < 1 or int(sys.argv[1]) > 20:
    print("timer range between 1 - 20")
    exit(1)
elif len(POMODORO_TIMER_MINUTES) == 2:
    POMODORO_TIMER_MINUTES = POMODORO_TIMER_MINUTES + ':00'
elif len(POMODORO_TIMER_MINUTES) == 1:
    POMODORO_TIMER_MINUTES = '0'+POMODORO_TIMER_MINUTES + ':00'
else:
    print("timer range between 1 - 20")
    exit(1)
TIMER = datetime.strptime(POMODORO_TIMER_MINUTES,'%M:%S')
sp.call('clear', shell=True)
print(TIMER.strftime("%M:%S"))
while True:
    if TIMER.strftime("%M:%S") == "00:00":
        sys.stdout.write('\a')
        print("Your pomodoro timer is up!")
        sys.stdout.flush()
        break
    time.sleep(1)
    TIMER = (TIMER - timedelta(seconds=1))
    sp.call('clear', shell=True)
    print(TIMER.strftime("%M:%S"))
