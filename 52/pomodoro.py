""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import timedelta
from time import sleep
import argparse


# default interval and break length values
INTERVAL_LENGTH = timedelta(minutes=25)
BREAK_LENGTH = timedelta(minutes=5)