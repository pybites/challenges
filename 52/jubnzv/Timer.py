# -*- coding: utf-8 -*-
"""
wxPomodoro - Simple pomodoro timer based on wxPython Phoenix GUI

The MIT License (MIT)
Copyright (C) 2017 Georgy Komarov <jubnzv@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""

import wx
import wx.adv
import datetime


class PomodoroTimer(wx.Timer):
    """Timer that includes desktop notifications on expire
    """

    # Timer status with UI name representation
    TIMER_STATUS = {'T_STOP': 'Stopped',
                    'T_RUN': 'Running',
                    'T_PAUSE': 'Paused',
                    'T_FINISH': 'Stopped'}
    TIMER_TICK = 1000  # Default tick interval == 1 second

    def __init__(self, dur, parent, id):
        """
        :param dur: Duration of timer (seconds)
        """
        super(PomodoroTimer, self).__init__(parent, id)

        self.frame = parent
        self.dur = dur
        self.t_remain = self.t_start = self.t_stop = self.t_tick = datetime.timedelta()
        self.status = self.TIMER_STATUS['T_STOP']

    def Notify(self):
        self.t_remain = self.t_remain - (datetime.datetime.now() - self.t_tick)
        self.t_tick = datetime.datetime.now()
        if self.t_remain.total_seconds() <= 0:  # Finish current cycle
            self.finish()

        super(PomodoroTimer, self).Notify()

    def start(self):
        """Runs the timer"""
        if self.status == self.TIMER_STATUS['T_STOP']:
            self.t_start = datetime.datetime.now()
            self.t_tick = self.t_start
            self.t_stop = self.t_start + datetime.timedelta(seconds=self.dur)
            self.t_remain = self.t_stop - self.t_start
        else:  # Timer already has been installed and was paused
            pass
        self.status = self.TIMER_STATUS['T_RUN']
        self.Start(self.TIMER_TICK)

    def stop(self):
        """Breaks existing timing data and stops the timer"""
        self.status = self.TIMER_STATUS['T_STOP']
        self.Stop()
        self.t_remain = self.t_start = self.t_stop = self.t_tick = datetime.timedelta()

    def pause(self):
        """Pause the timer"""
        self.status = self.TIMER_STATUS['T_PAUSE']
        self.Stop()

    def finish(self):
        """Represent 'Finish' state: timer expires successfully"""
        self.status = self.TIMER_STATUS['T_FINISH']
        self.Stop()
        self.t_remain = self.t_start = self.t_stop = self.t_tick = datetime.timedelta()

    def get_remain(self):
        """Returns remain time in timedelta"""
        return self.t_remain

    def get_status(self):
        """Returns a current status of timer"""
        return self.status

