from datetime import datetime, timedelta
import time


def main():

	print("Enter number of Pomodoro cycles (integer):")
	num_cycles =  input()

	print("Begin working!")

	for i in range(int(num_cycles)):
		for j in range(3):
			print("Work! Cycle " + str(i + 1) + ":")
			timer(datetime.now(), 0, 2)
			if(j != 3):
				print("Short Break!")
				timer(datetime.now(), 0, 2)
		print("Long break!")
		timer(datetime.now(), 0, 6)

	print("Done!")

def timer(start_time, countdown_minutes, countdown_seconds):
	end_time = start_time + timedelta(minutes = countdown_minutes, seconds = countdown_seconds)
	#print(((end_time - start_time).seconds)%5)
	# print(countdown_seconds)
	while(end_time > datetime.now()):
		minutes_left = str((end_time - datetime.now()).seconds / 60)
		seconds_left = str((end_time - datetime.now()).seconds % 60)
		print("\tWaiting ..." + minutes_left + "m " + seconds_left + "s " + "left...")
		time.sleep(2)



if __name__ == '__main__':
	main()