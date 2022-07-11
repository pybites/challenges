from datetime import datetime, timedelta
import time as time

def header():
	print(f'\nWelcome to your very own Pomodoro Timer!\n\n'
		f'--------------INSTRUCTIONS----------------\n'
		f'Start the Pomodoro timer\n'
		f'Work until the Pomodoro rings\n'
		f'Take a short break (5 minutes)\n'
		f'Keep on working, Pomodoro after Pomodoro, until the task at hand is finished.\n'
		f'Every 3 Pomodoros take a longer break, (15–30 minutes).\n'
		f'Enter how many sets do you want. (Each set has 3 Pomodoros)')
	set_loop(int(input()))

def set_loop(ans):
	while ans:
		for i in range(3):
			print('Time to work!')
			start_timer(25)
			print('Time to take a short break!')
			start_timer(5)
		print('Time to take a long break!')
		start_timer(10)
		ans-=1
	print('Congratulations for finishing!')

def start_timer(Minutes):
	timer = timedelta(minutes=Minutes)
	while timer:
		print(f'Time remaining: {str(timer)}')
		time.sleep(1)
		timer -= timedelta(seconds=1)
	print('Time is up!')

	

if __name__ == '__main__':
	header()