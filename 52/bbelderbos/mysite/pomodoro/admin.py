from django.contrib import admin

from pomodoro.models import Pomodoro


class PomodoroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pomodoro, PomodoroAdmin)
