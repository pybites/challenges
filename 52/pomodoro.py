""" PCC52 - Create your own Pomodoro Timer (24th of Sept 2018)
    Instructions + submit work: https://codechalleng.es/challenges/52"""

from datetime import timedelta
from time import sleep
import argparse


# default interval and break length values
INTERVAL_LENGTH = timedelta(minutes=25)
BREAK_LENGTH = timedelta(minutes=5)


def interval_countdown(sessions):
	'''Timer-like function to keep track of a single session.

	Args:
		param1 (int): number of sessions left.
	'''
	interval = INTERVAL_LENGTH
	while interval:
		interval -= timedelta(seconds=1)
		sleep(1)
		remaining_sessions = f'Remaininig sessions: {sessions}'
		print(f'{interval} - {remaining_sessions}\t\t\t', end='\r')