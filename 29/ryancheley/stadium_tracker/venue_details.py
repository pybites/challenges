import requests
from django.db.models import Count
from stadium_tracker.models import GameDetails


def get_venue_details(venue_id):
    url = f'http://statsapi.mlb.com/api/v1/venues/{venue_id}'
    response = requests.get(url)
    venue_name = None
    if response.status_code == 200:
        venue_name = response.json().get('venues')[0].get('name')
    return venue_name

def get_venue_total(venue_id):
    venue_total = list(GameDetails.objects.all().values('venue_id').annotate(total=Count('venue_id'))\
            .filter(venue_id=venue_id).values('total'))
    return venue_total

def get_venue_list(sportId, division_id):
    d = division_id
    url = 'http://statsapi.mlb.com/api/v1/teams'
    params = {
        'sportId': sportId
    }
    r = requests.get(url, params)
    teams = r.json().get('teams')
    venues = []
    for t in teams:
        team_name = t.get('name')
        venue_name = t.get('venue').get('name')
        venue_id = t.get('venue').get('id')
        visit_count = get_venue_total(venue_id)
        if len(visit_count) >0:
            visit_count = visit_count[0].get('total')
        else:
            visit_count = 0
        league_id = t.get('league').get('id')
        division_id = t.get('division').get('id')
        data = {
            'team_name': team_name,
            'venue_name': venue_name,
            'venue_id': venue_id,
            'league_id': league_id,
            'division_id': division_id,
            'user_visited': None,
            'visit_count': visit_count,
        }
        if d == division_id:
            venues.append(data)
        venues = sorted(venues, key=lambda venue: (venue['venue_name']))

    return venues

