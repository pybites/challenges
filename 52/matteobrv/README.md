# Pomodoro Timer
> *A barebone Pomodoro Timer application developed for the Pybites coding challenge #52.*

![Python version][python-version]

## Usage
Currently the utility is very basic. It just requires the user to
specify the number of sessions that they wish to run.
For instance, running only two sessions would require the application to be launched as follows:
```bash
python pomodoro.py -s 2
```
If you are executing it from MinGW, make sure to use the -u flag to avoid buffering related issues:
```bash
python -u pomodoro.py -s 2
```

## Help
If needed, more information are provided by the built in help feature:
```bash
pomodoro.py --help
usage: Pomodoro Timer [-h] -s SESSIONS

A barebone implementation of the Pomodoro timer. The program allows the user
to specify the number of sessions they wish to run; each session lasts 25
minutes and is followed by a break lasting 5 minutes.

optional arguments:
  -h, --help            show this help message and exit
  -s SESSIONS, --sessions SESSIONS
                        Number of 25 minute sessions you want to run

```
## Future improvements

* OOP refactoring
* allow the user to specify interval and break length 
* implement some form of GUI


[python-version]:https://img.shields.io/badge/python-3.7.3-brightgreen.svg
