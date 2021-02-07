from datetime import datetime

from django.shortcuts import render
from django.views.generic import TemplateView
from content.models import Content
from stadium_tracker.models import GameDetails
from stadium_tracker.game_details import get_games_for_date


class ContentTemplateView(TemplateView):
    model = Content
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if 'name' in self.kwargs.keys():
            title = self.kwargs['name']
        else:
            title = 'Stadia Tracker'
        data['pages'] = Content.objects.get(title=title)
        data['games'] = GameDetails.objects.all().order_by('-create_date')[:3]
        data['today'] = get_games_for_date(1, datetime.strftime(datetime.now(), '%Y-%m-%d'))
        return data
