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

import argparse

APP_VERSION = '0.1'
APP_NAME = 'wxPomodoro'

def get_args():
    """Parse and returns command line arguments"""
    parser = argparse.ArgumentParser(description=APP_NAME+': Simple pomodoro timer')

    parser.add_argument('--no-icon', action='store_false',
                        dest='show_icon', help='disable tray icon')
    parser.add_argument('--no-notify', action='store_false',
                        dest='show_notify', help='mute desktop notifications')
    parser.add_argument('-v', '--version', action='version',
                        version=APP_VERSION)

    args = parser.parse_args()
    return vars(args)

def start_app(cl_args):
    """Execute GUI application

    :param cl_args: Dict with command-line arguments
    """
    import wx
    from MainFrame import MainFrame

    app = wx.App()
    frame = MainFrame(parent=None, app_creds=(APP_NAME, APP_VERSION), cl_args=cl_args)
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    args = get_args()
    start_app(cl_args=args)
