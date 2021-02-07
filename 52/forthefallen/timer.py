from datetime import datetime
from datetime import timedelta
from time import sleep

def createEndTime(time):
    return (datetime.now() + timedelta(minutes=time))


def startTimer(endTime):
    while datetime.now() < endTime:
        sleep(1)
    print("Times Up")

startTimer(createEndTime(20))
