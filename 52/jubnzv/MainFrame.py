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
import datetime
import time
from collections import deque

from TaskBarIcon import TimerTaskBarIcon
from Timer import PomodoroTimer
from Notify import PomodoroNotify


class StatusTextCtrl(wx.TextCtrl):
    """Custom TextCtrl using to represent status on a timer panel"""

    def __init__(self, *args, **kwargs):
        super(StatusTextCtrl, self).__init__(*args, **kwargs)
        parent = args[0]
        self.SetBackgroundColour(parent.GetBackgroundColour())
        self.SetEditable(False)
        self.Bind(wx.EVT_SET_FOCUS, self.OnFocus)

    def OnFocus(self, event):
        """Disable focus event"""
        self.Navigate()


class MainFrame(wx.Frame):
    """Main frame of program
    """

    TIME_UNITS = ['sec', 'min', 'hour']

    def __init__(self, app_creds, cl_args, *args, **kwargs):
        """
        :param app_creds: Tuple with application name and version values
        :type app_creds: tuple
        :param cl_args: Dict that contents user-defined application options
        """
        super(MainFrame, self).__init__(*args, **kwargs)

        self.app_name, self.app_version = app_creds

        # Timer initialization
        self.timer = None  # Current timer
        self.timers_queue = deque()
        self.timers_count = 0
        self.p_dur = self.sb_dur = self.lb_dur = 0
        self.timer_status = None

        # Status & notifications elements
        self.current_task = 'Waiting'
        self.notify_controller = None
        self.tbIcon = None

        # Intiailize the UI
        self.mainPanel = wx.Panel(self)
        self.mainSz = wx.BoxSizer(wx.VERTICAL)

        self._initStatusPanel()
        self._initTimerPanel()
        self._initControlButtons()
        self._setTitle()

        if cl_args['show_notify']:
            self._initNotify()

        if cl_args['show_icon']:
            self._initTrayIcon()
            self.Bind(wx.EVT_CLOSE, self.Minimize)
        else:
            self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.mainSz.Fit(self)
        self.mainPanel.SetSizer(self.mainSz)

        self.Refresh()

    def _initStatusPanel(self):
        """Initialize the status panel that represents current pomodoro state"""
        self.statusPanel = wx.StaticBox(self.mainPanel, wx.ID_ANY, label='Current status')
        statusSz = wx.StaticBoxSizer(self.statusPanel)
        statusElsSz = wx.GridBagSizer(vgap=5, hgap=5)

        self.currentTime = StatusTextCtrl(self.statusPanel, wx.ID_ANY, style=wx.TE_READONLY)
        self._setCurrentTime()  # Set default zeroed value
        statusElsSz.Add(self.currentTime, pos=(0,0), flag=wx.EXPAND|wx.ALL, border=3)

        self.currentStatus = StatusTextCtrl(self.statusPanel, wx.ID_ANY, style=wx.TE_READONLY)
        self._setCurrentStatus()
        statusElsSz.Add(self.currentStatus, pos=(0,2), flag=wx.EXPAND|wx.ALL, border=3)

        self.currentTask = StatusTextCtrl(self.statusPanel, wx.ID_ANY, style=wx.TE_READONLY)
        self._setCurrentTask()
        statusElsSz.Add(self.currentTask, pos=(0,3), flag=wx.EXPAND|wx.ALL, border=3)

        statusElsSz.AddGrowableCol(1)
        statusElsSz.AddGrowableRow(0)
        statusSz.Add(statusElsSz, proportion=1, flag=wx.ALL|wx.EXPAND)
        self.mainSz.Add(statusSz, flag=wx.ALL|wx.EXPAND, border=10)

    def _initTimerPanel(self):
        """Initialize the timer panel"""
        timerPanel = wx.StaticBox(self.mainPanel, wx.ID_ANY, label='Timer options')
        timerSz = wx.StaticBoxSizer(timerPanel)
        timerOptSz = wx.FlexGridSizer(rows=4, cols=3, vgap=10, hgap=8)

        # Pomodoro duration
        pDurationLabel = wx.StaticText(timerPanel, wx.ID_ANY, label='Pomodoro')
        self.pDurationVal = wx.SpinCtrl(timerPanel, wx.ID_ANY, style=wx.TE_RIGHT, initial=25,
                                         min=1, max=3600)
        self.pDurationUnit = wx.Choice(timerPanel, wx.ID_ANY, choices=self.TIME_UNITS)
        self.pDurationUnit.SetSelection(1)
        timerOptSz.Add(pDurationLabel, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=3)
        timerOptSz.Add(self.pDurationVal, flag=wx.ALL|wx.EXPAND, border=3)
        timerOptSz.Add(self.pDurationUnit, flag=wx.ALL|wx.EXPAND, border=3)

        # Short break duration
        sbDurationLabel = wx.StaticText(timerPanel, wx.ID_ANY, label='Short break')
        self.sbDurationVal = wx.SpinCtrl(timerPanel, wx.ID_ANY, style=wx.TE_RIGHT, initial=5,
                                         min=1, max=3600)
        self.sbDurationUnit = wx.Choice(timerPanel, wx.ID_ANY, choices=self.TIME_UNITS)
        self.sbDurationUnit.SetSelection(1)
        timerOptSz.Add(sbDurationLabel, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=3)
        timerOptSz.Add(self.sbDurationVal, flag=wx.ALL|wx.EXPAND, border=3)
        timerOptSz.Add(self.sbDurationUnit, flag=wx.ALL|wx.EXPAND, border=3)

        # Long break duration
        lbDurationLabel = wx.StaticText(timerPanel, wx.ID_ANY, label='Long break')
        self.lbDurationVal = wx.SpinCtrl(timerPanel, wx.ID_ANY, style=wx.TE_RIGHT, initial=30,
                                         min=1, max=3600)
        self.lbDurationUnit = wx.Choice(timerPanel, wx.ID_ANY, choices=self.TIME_UNITS)
        self.lbDurationUnit.SetSelection(1)
        timerOptSz.Add(lbDurationLabel, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=3)
        timerOptSz.Add(self.lbDurationVal, flag=wx.ALL|wx.EXPAND, border=3)
        timerOptSz.Add(self.lbDurationUnit, flag=wx.ALL|wx.EXPAND, border=3)

        # Pomodoros to long break
        cntLabel = wx.StaticText(timerPanel, wx.ID_ANY, label='Pomodoros to break')
        self.cntVal = wx.SpinCtrl(timerPanel, wx.ID_ANY, initial=4, min=1, max=1000,
                                  style=wx.SP_ARROW_KEYS|wx.ALIGN_LEFT)
        timerOptSz.Add(cntLabel, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL)
        timerOptSz.Add(self.cntVal, flag=wx.ALL|wx.EXPAND)

        timerOptSz.AddGrowableCol(0)
        timerSz.Add(timerOptSz, flag=wx.EXPAND|wx.ALL, border=10)
        self.mainSz.Add(timerSz, flag=wx.EXPAND|wx.ALL, border=10)

    def _initControlButtons(self):
        """Initialize the control buttons in a bottom of MainFrame"""
        btnSz = wx.GridBagSizer(vgap=4, hgap=4)

        self.startBut = wx.Button(self.mainPanel, wx.ID_ANY, label='Start')
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.startBut)
        btnSz.Add(self.startBut, pos=(0,1), flag=wx.ALL|wx.EXPAND, border=3)

        self.pauseBut = wx.Button(self.mainPanel, wx.ID_ANY, label='Pause')
        self.Bind(wx.EVT_BUTTON, self.OnPause, self.pauseBut)
        btnSz.Add(self.pauseBut, pos=(0,2), flag=wx.ALL|wx.EXPAND, border=3)

        self.stopBut = wx.Button(self.mainPanel, wx.ID_ANY, label='Stop')
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.stopBut)
        btnSz.Add(self.stopBut, pos=(0,3), flag=wx.ALL|wx.EXPAND, border=3)

        self.startBut.SetFocus()
        btnSz.AddGrowableRow(0)
        btnSz.AddGrowableCol(0)
        self.mainSz.Add(btnSz, flag=wx.ALIGN_RIGHT|wx.EXPAND, border=10)

    def _initTrayIcon(self):
        """Initialize tray icon and minimize-restore routines"""
        self.tbIcon = TimerTaskBarIcon(self)
        self.Bind(wx.EVT_ICONIZE, self.Minimize)

    def _initNotify(self):
        """Initialize notifications"""
        self.notify_controller = PomodoroNotify(app_name=self.app_name)

    def _cleanIcon(self):
        """Remove taskbar icon"""
        if self.tbIcon:
            self.tbIcon.RemoveIcon()
            self.tbIcon.Destroy()

    def queue_init(self):
        """Setup the PomodoroTimer queue

        Timers queue used to implement full pomodoro stack: from start to long break.
        """
        self.timers_queue = deque()
        for i in range(self.timers_count):
            self.timers_queue.append(('Pomodoro', PomodoroTimer(dur=self.p_dur, parent=self, id=wx.ID_ANY)))
            self.timers_queue.append(('Short break', PomodoroTimer(dur=self.sb_dur, parent=self, id=wx.ID_ANY)))
        self.timers_queue[-1] = (('Long break', PomodoroTimer(dur=self.lb_dur, parent=self, id=wx.ID_ANY)))

    def queue_clean(self):
        """Remove all timers from queue"""
        self.timers_qeueue = deque()
        self.timer = None
        self.timer_status = None

    def queue_next(self):
        """Starts the next timer from queue"""
        self.current_task = self.timers_queue[0][0]  # Type of current timer
        self.timer = self.timers_queue[0][1]  # Timer object
        self.timer.start()
        self.timer_status = self.timer.get_status()
        self.Bind(wx.EVT_TIMER, self.TimerLoop)
        self.timers_queue.popleft()
        if self.notify_controller:
            self.notify_controller.show_status(self.current_task)

    def Refresh(self):
        """Update panel contents"""
        self._setCurrentStatus()
        self._setCurrentTask()

        # Update timer status color
        if self.timer_status == PomodoroTimer.TIMER_STATUS['T_RUN']:
            self.currentTime.SetBackgroundColour((255, 255, 255))
        else:
            self.currentTime.SetBackgroundColour(self.statusPanel.GetBackgroundColour())

        # Update app icon
        if self.tbIcon:
            self.tbIcon.set_status(self.timer_status)

        # Update control buttons according current timer status
        if self.timer_status == PomodoroTimer.TIMER_STATUS['T_RUN']:
            self.startBut.Disable()
            self.pauseBut.Enable()
            self.stopBut.Enable()
        elif self.timer_status == PomodoroTimer.TIMER_STATUS['T_PAUSE']:
            self.startBut.Enable()
            self.pauseBut.Disable()
            self.stopBut.Enable()
        else:  # Stopped or finished
            self.startBut.Enable()
            self.pauseBut.Disable()
            self.stopBut.Disable()

        self._setCurrentTime()
        self._setTitle()

    def format_timedelta(self, td):
        """Format timevalue in seconds to HH:MM:SS format

        :type td: datetime.timedelta
        """
        h = td.seconds // 3600
        m, s = divmod(td.seconds, 60)
        return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

    def _setCurrentStatus(self):
        """Set current status in UI"""
        if not self.timer:
            self.timer_status = PomodoroTimer.TIMER_STATUS['T_STOP']
        else:
            self.timer_status = self.timer.get_status()
        self.currentStatus.SetValue(self.timer_status)

    def _setCurrentTask(self):
        """Set current task type (work / short break / long break) in UI"""
        self.currentTask.SetValue(self.current_task)

    def _setCurrentTime(self):
        """Sets actual timer value to currentTime element"""
        if self.timer:
            remain = self.format_timedelta(self.timer.get_remain())
        else:
            remain = '00:00:00'
        self.currentTime.SetValue(remain)

    def _setTitle(self):
        """Change frame's title according timer current status"""
        if self.timer_status in (PomodoroTimer.TIMER_STATUS['T_RUN'], PomodoroTimer.TIMER_STATUS['T_RUN']):
            remain = self.format_timedelta(self.timer.get_remain())
            title = ' '.join([self.app_name, self.timer_status.lower(), remain, 'left'])
        else:  # Stopped or finished
            title = self.app_name+ ' ' + self.timer_status.lower()

        self.SetTitle(title)

    def _getUserInput(self):
        """Get input from UI forms"""
        def get_secs(valElement, unitElement):
            """Return current time in seconds according time unit choice in UI"""
            val = valElement.GetValue()
            if unitElement.GetSelection() == 0:  # seconds
                return int(val)
            if unitElement.GetSelection() == 1:  # minutes
                return int(val)*60
            if unitElement.GetSelection() == 2:  # hours
                return int(val)*3600

        self.p_dur = get_secs(self.pDurationVal, self.pDurationUnit)
        self.sb_dur = get_secs(self.sbDurationVal, self.sbDurationUnit)
        self.lb_dur = get_secs(self.lbDurationVal, self.lbDurationUnit)
        self.timers_count = self.cntVal.GetValue()

    def TimerLoop(self, event):
        self.timer_status = self.timer.get_status()
        if self.timer_status == PomodoroTimer.TIMER_STATUS['T_FINISH'] and self.timers_queue:
            self.queue_next()
        self.Refresh()

    def OnStart(self, event):
        self._getUserInput()
        self.queue_init()
        self.queue_next()
        self.timer.start()
        if self.notify_controller:
            self.notify_controller.show_action('Started!')
        self.stopBut.SetFocus()
        self.Refresh()

    def OnPause(self, event):
        self.timer.pause()
        if self.notify_controller:
            self.notify_controller.show_action('Paused')
        self.Refresh()

    def OnStop(self, event):
        self.timer.stop()
        self.queue_clean()
        if self.notify_controller:
            self.notify_controller.show_action('Stopped')
        self.startBut.SetFocus()
        self.Refresh()

    def Minimize(self, event):
        """Minimize to tray"""
        self.Hide()

    def Exit(self):
        """Close this frame

        It should be called from external, if we bind Minimize on EVT_CLOSE
        """
        self._cleanIcon()
        self.Destroy()
        self.Close()

    def OnClose(self, event):
        if event.CanVeto() and self.timer_status == PomodoroTimer.TIMER_STATUS['T_RUN']:
            if wx.MessageBox('Timer already started. Exit now?',
                             'Please confirm',
                             wx.ICON_QUESTION | wx.YES_NO) != wx.YES:
                event.Veto()
                return

        self._cleanIcon()
        self.Destroy()
