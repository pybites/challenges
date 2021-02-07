from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from StadiumTrackerAPI import settings
from django.utils import timezone


class GameDetails(models.Model):
    home_team = models.CharField(max_length=100)
    home_runs = models.IntegerField()
    home_hits = models.IntegerField(blank=True, null=True)
    home_errors = models.IntegerField(blank=True, null=True)
    away_team = models.CharField(max_length=100)
    away_runs = models.IntegerField()
    away_hits = models.IntegerField(blank=True, null=True)
    away_errors = models.IntegerField(blank=True, null=True)
    game_datetime = models.DateTimeField()
    game_headline = models.CharField(max_length=254, blank=True, null=True)
    game_body = models.TextField(blank=True, null=True)
    game_id = models.IntegerField()
    venue_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} ({self.game_datetime.strftime("%m/%d/%Y")})'

    def save(self, *args, **kwargs):
        self.modify_date = timezone.now()
        super(GameDetails, self).save(*args, **kwargs)

    def get_venue_count(self):
        game_venue = []
        details = GameDetails.objects.all().values('venue_id').annotate(total=Count('venue_id')).order_by('-total')
        for d in details:
            game_venue.append({
                'venue_id': d.get('venue_id'),
                'total': d.get('total')
            })
        return game_venue

    class Meta:
        unique_together = ['user', 'game_id',]
        ordering=['user', '-game_datetime']
