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


def break_countdown(sessions):
	'''Timer-like function to keep track of a single break.

	Args:
		param1 (int): number of sessions left.
	'''
	_break = BREAK_LENGTH
	while _break and sessions >= 1:
		_break -= timedelta(seconds=1)
		sleep(1)
		print(f'Take a break! You have {_break} until the next session', end='\r')


def run_pomodoro(user_input):
	'''Timer-like function to keep track of the
	number of sessions that are left.

	Args:
		param1 (int): number of sessions the user wish the timer to run.
	'''
	sessions = user_input
	while sessions:
		interval_countdown(sessions)
		sessions -= 1
		break_countdown(sessions)
	print('All done!\t\t\t')


def parse_args():
	parser = argparse.ArgumentParser(
		prog='Pomodoro Timer',
		description='''A barebone implementation of the Pomodoro timer.
		The program allows the user to specify the number of sessions they wish to run;
		each session lasts 25 minutes and is followed by a break lasting 5 minutes.''')
	parser.add_argument(
		'-s',
		'--sessions',
		type=int,
		action='store',
		required=True,
		help='Number of 25 minute sessions you want to run')

	return parser.parse_args()


def main(args):
	run_pomodoro(args.sessions)


if __name__ == '__main__':
	args = parse_args()
	main(args)