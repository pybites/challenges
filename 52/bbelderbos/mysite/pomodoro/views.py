from collections import defaultdict

from django.contrib import messages
from django.shortcuts import render

from pomodoro.models import (Pomodoro,
                             DEFAULT_POMO_GOAL,
                             DEFAULT_POMO_MIN,
                             this_week)


def track_pomodoro(request):
    post = request.POST
    user = request.user.is_authenticated and request.user or None

    if post.get('add'):
        new_pomo = Pomodoro(user=user)  # rest fields = defaults
        new_pomo.save()
        msg = 'Great job, another pomodoro done!'
        messages.success(request, msg)

    pomodori = Pomodoro.objects.all()
    if user:
        pomodori = pomodori.filter(user=request.user)

    week_stats = defaultdict(list)
    for pomo in pomodori:
        week_stats[pomo.week].append(1)

    pomos_done = len(week_stats.get(this_week(), 0))
    pomos_todo = [1] * (DEFAULT_POMO_GOAL - pomos_done)
    if pomos_done == DEFAULT_POMO_GOAL:
        msg = ('\nAwesome, you hit the 5 hour rule this week! '
               'You are well away to the top!!')
        messages.success(request, msg)

    return render(request,
                  'pomodoro/pomodoro.html',
                  {'week_stats': week_stats.items(),
                   'week_goal': DEFAULT_POMO_GOAL,
                   'pomo_minutes': DEFAULT_POMO_MIN,
                   'pomos_todo': pomos_todo
                   })
