#!/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt
import time

statusDict = {
              "working" : [20, "get to work"],
              "short break" : [5, "take a short break"],
              "long break" : [15, "take a long break"],
}


class pomodoro_timer(object):

    def __init__(self):
        print ("Timer started!!!")
        self.status = "working"
        self.pCount = 0
        self.timer()
        

    def timer(self):

        print ("Let's {}!!!".format(statusDict[self.status][1]))
        loopCount = statusDict[self.status][0]
        print ("{} minutes to go...".format(loopCount))
        self.__time = dt.datetime.now()
        while loopCount > 0:
            while self.__time + dt.timedelta(seconds=60) > dt.datetime.now():
                pass
            else:
                self.__time = dt.datetime.now()
                loopCount -= 1
                if loopCount == 1:
                    print ("{} minute to go...".format(loopCount))
                else: 
                    print ("{} minutes to go...".format(loopCount))     
        else:
            print (" ")
            if self.status == "working":
                if self.pCount < 3:
                    self.pCount += 1
                    self.status = "short break"
                else:
                    self.pCount = 0
                    self.status = "long break"
            else:
                self.status = "working"

        self.timer()


def main():

    print ("""
Author: Russell Brown
E-Mail: rkb.5476@gmail.com
Version: 1.0
Name: Pomodoro Timer
Description: This tool will notify the user when to work and when to take breaks, and for how long.
             The user will work for 20 minutes, then get a 5 minute break. The user will get a 15 minute
             break after 4 working sessions (pomodoros).
Use: Press 'CTRL-C' to stop the timer.
""")

    startTime = dt.datetime.now()
    try:
        a = pomodoro_timer()
    except KeyboardInterrupt:
        endTime = dt.datetime.now()
        print ("\nStarted Working: {}".format(startTime))
        print ("Finished Working: {}".format(endTime))
        print ("Total Time Worked: {}\n".format(endTime - startTime))

    input("Strike ENTER key to exit...")



if __name__ == "__main__":
    main()
    





        


