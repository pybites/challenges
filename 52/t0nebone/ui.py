from pomodoro import pom_timer

wt = int(input('Enter the duration in minutes you would like your work sessions to be:'))
bt = int(input('Enter the duration in minutes you would like your breaks to be:'))
rds = int(input('How many rounds would you like to do'))

pom_timer(wt, bt, rds)
