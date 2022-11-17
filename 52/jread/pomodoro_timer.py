import time

from datetime import datetime
from datetime import timedelta

# Note - this Pomodoro timer uses seconds instead of minutes for practical reasons - a real Pomodoro timer would use
# minutes instead

# Start time is now
start = datetime.now()

# Run timer for this duration
duration = timedelta(seconds=60)

# Stop the timer once duration is reached
stop = start + duration

# Take breaks at this frequency
break_frequency = timedelta(seconds=25)

# Breaks are this duration
break_duration = timedelta(seconds=5)

# Work status - working or break
work_status = 'working'

# When to take the first break (transition from work to break)
next_transition = start + break_frequency

# Seconds counter
secs = 0

print(f'Starting pomodoro timer [start_time={start}] [stop_time={stop}] [break_frequency={break_frequency}] '
      f'[first_break={next_transition}')

# Run the timer from now until the stop time designated above
while datetime.now() < stop:
    # If at a transition time (ignore milliseconds), then change the status from working => break or break => working
    # and set the next transition time (+5 if transitioning to break, +25 if transitioning to work)
    if str(datetime.now()).split('.')[0] == str(next_transition).split('.')[0]:
        next_transition = datetime.now() + (break_duration if work_status == 'working' else break_frequency)
        work_status = 'break' if work_status == 'working' else 'working'
    secs += 1
    print(f'[{secs:03}] Work status={work_status}')
    time.sleep(1)
