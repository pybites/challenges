from datetime import datetime
import time

DURATION = 10

def pomodoro(duration):
    print(f'Starting Pomodoro timer for {duration} minutes.')
    print(f'Start time: {current_time()}')
    time.sleep(duration*60)
    print(f'End time: {current_time()}')

def current_time():
    return((datetime.now().strftime("%Y-%m-%d %H:%M")))

if __name__ == "__main__":
    pomodoro(DURATION)

