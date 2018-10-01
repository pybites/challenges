from datetime import date, timedelta

from django.db import models
from django.contrib.auth.models import User

# "5 hour rule" would be 12 pomodori of 25 min
# = good reading defaults
DEFAULT_POMO_GOAL, DEFAULT_POMO_MIN = 12, 25
TODAY = date.today()


def this_week(dt=TODAY):
    return f'{dt.strftime("%Y")}/{dt.isocalendar()[1]}'


class Pomodoro(models.Model):
    # in case we use it in a project with login
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True)
    # a counter would be enough but keeping track of minutes in case
    # we want various pomodori sizes
    minutes = models.IntegerField(default=DEFAULT_POMO_MIN)
    # pomodoro will be added upon finishing the pomo
    end = models.DateTimeField(auto_now_add=True)

    @property
    def start(self):
        """Deduct start time calculating # minutes back from self.end"""
        return self.end - timedelta(minutes=self.minutes)

    @property
    def week(self):
        """Deduct YYYY-WW (year/week) from end datetime"""
        return this_week(self.end)

    def __str__(self):
        return (f'{self.user} - {self.minutes} '
                f'({self.start}-{self.end})')

    class Meta:
        ordering = ['-end']
