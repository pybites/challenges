POMODORO APPLICATION

Application needs speech-dispatcher to run, you can use command:
sudo apt install speech-dispatcher to install it on Linux if you're using Windows 
probably you need to comment out lines when speed dispatcher is used (comments in code will point you which parts)

You can use application with the command :
python pomodoro.py(or your name for the app if you changed it)
you can add your values to the configuration using following arguments:
--duration, type=integer, default=20, you will choose duration length of one pomodoro iteration, it's represented in minutes
--br_legth, type=integer, default=5, you will choose duration length of break, it's represented in minutes
--count, type=integer, default=4, you will choose how many time you want to repeat process

example:
python pomodoro.py --iteration 5 --br_length 2 --count 2
with such command you will have pomodoro timer with pomodoro iteration with length 5minutes,
break time equals 2 minutes and process will be repeated 2 times

