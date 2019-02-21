""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

# Author : Gaurav Pawar (gp1313)

from datetime import datetime
from datetime import date
import argparse
import time

def main():
    iTPmins = 2
    print('Timer starts!!')
    oStartTimeStamp = datetime.now()
    while(True) :
        time.sleep(1)
        oTimeDelta =  datetime.now() - oStartTimeStamp
        if oTimeDelta.seconds > (iTPmins * 60.0):
            break
    print('Timer ends')

if __name__ == '__main__' :
    main()
