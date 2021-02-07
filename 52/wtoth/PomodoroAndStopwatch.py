from datetime import datetime
from datetime import timedelta

import sys

def starttimer(lengthminutes):
	end = False
	timenow = datetime.now()
	endtime = timedelta(minutes=lengthminutes)+timenow
	print("The Timer will end at " + str(endtime.strftime("%I:%M:%S %p")))
	try:
		while(end == False):
			if(datetime.now() >= endtime):
				print("Timer Done")
				end = True
	except KeyboardInterrupt:
		print("Timer Cancelled")
		sys.exit()

def startstopwatch():
	starttime = datetime.now()
	stoptime = datetime.now()
	stop = False
	while(stop == False):
		value = input("Type Stop to end stopwatch\n")
		if(str(value) == "stop" or str(value) == "Stop"):
			stoptime = datetime.now()
			stop = True
	print("Start: " + str(starttime) + "\nStop: " + str(stoptime))
	print("Time Elapsed: " + str(stoptime - starttime))