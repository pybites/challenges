# 🍅 `cl_pomodoro`
## Time your study sessions!
`cl_pomodoro.py` is a simple command line Pomodoro timer, designed for 
timed study sessions. It was created during my #100DaysOfCode programme, 
after two sessions focused around `datetime`.

## About

- `cl_pomodoro` takes the current time and, given a study session 
length, tells the user when their study period will end.
- It displays a timer of minutes and seconds remaining.

## How to

**usage**: `$ cl_pomodoro.py [-h] [-a] study`

**positional arguments**:
  study        minutes in study period (integer)

**optional arguments**:
  -h, --help   show this help message and exit
  -a, --alarm  'beep' when study period is over

Note that the alarm is _off_ by default. Only by passing the alarm 
argument will the user hear a 'beep'.

📚 Study well, my friend!