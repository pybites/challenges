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

import pgi
pgi.require_version('Notify', '0.7')
from pgi.repository import Notify


class PomodoroNotify:
    """Notification wrapper
    """
    def __init__(self, app_name):
        self.app_name = app_name
        Notify.init(app_name)

    def _show_notify(self, text='', urg=0):
        """Shows notification via libnotify"""
        status = Notify.Notification.new(self.app_name, text, 'dialog-information')
        status.set_urgency(urg)
        status.show()

    def show_status(self, status):
        """Shows current status"""
        status = ' '.join(['Current stage:', status])
        self._show_notify(text=status)

    def show_action(self, action):
        """Shows current action e.g. pause, stop, run"""
        self._show_notify(text=action, urg=1)

