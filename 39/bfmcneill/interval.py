"""This module builds an interval object that can be used in code that requires timers such as pomodor timers"""

from datetime import datetime, timedelta


def datetime_round(dt=None):
    """helper function that truncates a date time object to the nearest second"""
    if not dt:
        dt = datetime.now()

    if dt.microsecond >= 500000:
        dt = dt + timedelta(seconds=1)

    dt = dt.replace(microsecond=0)

    return dt


"""This dictionary helps make the interval status code friendly for humans"""
interval_states = {"ACTIVE": 1, "COMPLETE": 2, "INITIAL": 3}


class Interval:
    '''Interval object holds details about the start and stop times of an event'''

    def __init__(self):
        self.status = interval_states["INITIAL"]
        self.datetime_begin = None
        self.datetime_expire = None

    def begin(self):
        '''open the interval'''
        if self.status in [interval_states["ACTIVE"], interval_states["COMPLETE"]]:
            raise ValueError("Interval has already been initiated")

        self.datetime_begin = datetime_round()
        self.status = interval_states["ACTIVE"]

    def expire(self):
        '''close the interval'''
        if self.status in [interval_states["COMPLETE"], interval_states["INITIAL"]]:
            raise ValueError("Interval must be in process")

        self.datetime_expire = datetime_round()
        self.status = interval_states["COMPLETE"]

    def durration_calc(self):
        '''determine the length of the closed interval in seconds'''
        if self.status in [interval_states["INITIAL"], interval_states["ACTIVE"]]:
            raise ValueError("Interval is not complete")
        delta = self.datetime_expire - self.datetime_begin
        return delta.total_seconds()
