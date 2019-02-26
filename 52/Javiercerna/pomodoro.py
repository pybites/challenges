import datetime
import time
import sys

TIMER_END = datetime.timedelta(minutes=0)

timer = datetime.timedelta(minutes=20)

while timer != TIMER_END:
    print(timer, end='\r', flush=True)
    timer -= datetime.timedelta(seconds=1)
    time.sleep(1)

print(TIMER_END)
print('Pomodoro completed! Time for a break...')