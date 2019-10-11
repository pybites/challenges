from datetime import datetime,timedelta
import time
import os

timer_duration=int(input('How many minutes the timer should run::'))
break_duration=int(input('how long the break should be::'))
iter_count=int(input('how many times the Pomodoro timer should run::'))


def pomodoroTimer(duration,startTime):
    os.system('say "time to work" ')   #speech dispatcher
    print('pomodoro started at: {} and will end at: {}'.format(datetime.now(),datetime.now()
          +timedelta(minutes=duration)))
    
    timer=True

    while timer:
        workTime=datetime.now()-startTime
        if workTime>=timedelta(minutes=duration):
            timer=False
        


def breakTimer(duration,startTime):
    os.system('say "break time" ')     #speech dispatcher
    print('break started at: {} and should end at: {}'.format(datetime.now(),datetime.now()
          +timedelta(minutes=duration)))
    timer=True

    while timer:
        breakTime=datetime.now()-startTime
        if breakTime>=timedelta(minutes=duration):
            timer=False


for i in range(iter_count):
    if i==0:
        print("pomodoro started with the following configuration:")
        print('length of one pomodoro iteration: '+str(timer_duration)+' min')
        print('break length: '+str(break_duration)+ ' min')
        print('number of iterations: '+str(iter_count))
        pomodoroTimer(timer_duration,datetime.now())
        breakTimer(break_duration,datetime.now())

    
    elif i == iter_count-1:
        pomodoroTimer(timer_duration,datetime.now())
    else:
        pomodoroTimer(timer_duration,datetime.now())
        breakTimer(break_duration,datetime.now())
os.system('say "Thats good job Mate" ')    







