from datetime import datetime
from datetime import timedelta

time_duration = int(input('Enter time duration:' ))
start_time = datetime.now()
end_time = start_time + timedelta(minutes=time_duration)

while ((end_time - datetime.now())) >= timedelta(seconds=0):
    print(str(end_time - datetime.now()))

print('Alarm!')
