from datetime import datetime, timedelta
from dateutil import tz
import requests


def get_game_object(game_id):
    game_url = f'http://statsapi.mlb.com/api/v1/schedule/games?sportId=1&gamePk={game_id}'
    game = requests.get(game_url)
    return game

def get_game_story(game_id):
    story_url = f'http://statsapi.mlb.com/api/v1/game/{game_id}/content'
    story = requests.get(story_url)
    return story

def get_game_date(game_id):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    v = get_game_object(game_id).json().get('dates')[0].get('games')[0].get('gameDate')
    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%SZ')
    v = v.replace(tzinfo=from_zone)
    v = v.astimezone(to_zone)
    return v

def get_game_recap(game_id, type):
    story = get_game_story(game_id)
    data = None
    if story.status_code == 200 and story.json().get('editorial') is not None:
        recap = story.json().get('editorial').get('recap').get('mlb')
        if recap is not None:
            data = recap.get(f'{type}')
        return data

def get_venue_id(game_id):
    v = get_game_object(game_id).json().get('dates')[0].get('games')[0].get('venue').get('id')
    return v

def get_boxscore(game_id, type):
    boxscore_url = f'http://statsapi.mlb.com/api/v1/game/{game_id}/boxscore'
    r_boxscore = requests.get(boxscore_url)
    boxscore = r_boxscore.json()
    teams = boxscore.get('teams')
    if len(boxscore.get('teams').get('home').get('teamStats')) > 0:
        team = {
            'hits': teams.get(f'{type}').get('teamStats').get('batting').get('hits'),
            'runs': teams.get(f'{type}').get('teamStats').get('batting').get('runs'),
            'errors': teams.get(f'{type}').get('teamStats').get('fielding').get('errors'),
            'team': teams.get(f'{type}').get('team').get('name'),
        }
    else:
        team = {
            'hits': None,
            'runs': get_score(1, game_id, type),
            'errors': None,
            'team': get_game_object(game_id).json().get('dates')[0].get('games')[0].get('teams').get(f'{type}').get('team').get('name'),
        }
    return team

def get_score(sportId, gamePk, type):
    params = {
        'sportId': sportId,
        'gamePk': gamePk,
    }
    url = 'http://statsapi.mlb.com/api/v1/schedule/games'
    r = requests.get(url, params)
    score = None
    if r.json().get('dates'):
        games_date = r.json().get('dates')[0].get('date')
        home_team_id = r.json().get('dates')[0].get('games')[0].get('teams').get('home').get('team').get('id')
        away_team_id = r.json().get('dates')[0].get('games')[0].get('teams').get('away').get('team').get('id')
        teamId = f'{home_team_id},{away_team_id}'
        params2 = {
            'sportId': sportId,
            'teamId': teamId,
            'startDate': games_date,
            'endDate': games_date,
        }
        r2 = requests.get(url, params2)
        score = r2.json().get('dates')[0].get('games')[0].get('teams').get(f'{type}').get('score')
    return score


def get_teams(sportId) -> list:
    """
    :return: list of teams in alphabetical order
    """
    url = f'http://statsapi.mlb.com/api/v1/teams?sportId={sportId}'
    r = requests.get(url)
    teams = r.json().get('teams')
    teams = sorted(teams, key = lambda team: (team['name']))
    team_display = []
    for i in range(len(teams)):
        team_display.append({'id': teams[i].get('id'), 'name': teams[i].get('name')})
    return team_display


def get_team(teamId):
    url = f'http://statsapi.mlb.com/api/v1/teams?sportId=1&teamId={teamId}'
    r = requests.get(url)
    team = r.json().get('teams')[0].get('name')
    return team



def get_form_details(request):
    """

    :param request: the request object from the page
    :return: list of dictionaries
        text: String of Game
        gamePk: Int of the gamePk
    """
    sportId = 1
    team1 = request.GET.get('team1')
    team2 = request.GET.get('team2')
    teamId = f'{team1},{team2}'
    start_date = request.GET.get('start_date')
    # Commented line below as the search is only adding the first entry and not all entries returned
    # TODO: fix so that date range can be searched
    # end_date = request.GET.get('end_date')
    end_date = start_date
    params = {
        'sportId': sportId,
        'teamId': teamId,
        'startDate': start_date,
        'endDate': end_date
    }
    url = 'http://statsapi.mlb.com/api/v1/schedule/games'
    r = requests.get(url, params)
    games_dates = r.json().get('dates')
    display_dates = []
    if games_dates is not None:
        for i in range(len(games_dates)):
            date = games_dates[i].get('date')
            for j in range(len(games_dates[i].get('games'))):
                away = games_dates[i].get('games')[j].get('teams').get('away').get('team').get('name')
                away_id = games_dates[i].get('games')[j].get('teams').get('away').get('team').get('id')
                home = games_dates[i].get('games')[j].get('teams').get('home').get('team').get('name')
                home_id = games_dates[i].get('games')[j].get('teams').get('home').get('team').get('id')
                away_score = games_dates[i].get('games')[j].get('teams').get('away').get('score')
                home_score = games_dates[i].get('games')[j].get('teams').get('home').get('score')
                text = f'{date}: {away} vs {home}. Final Score: {away_score} - {home_score}'
                gamePk = games_dates[i].get('games')[j].get('gamePk')
                venue_id = games_dates[i].get('games')[j].get('venue').get('id')
                data = {
                    'text': text,
                    'gamePk': gamePk,
                    'venue_id': venue_id
                }
                if (str(home_id) == team1 and str(away_id) == team2) or (
                        str(home_id) == team2 and str(away_id) == team1):
                    display_dates.append(data)
    return display_dates


def get_default_game(sportId):
    url = 'http://statsapi.mlb.com/api/v1/schedule/games'
    game_date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    params = {
        'sportId': sportId,
        'startDate': game_date,
        'endDate': game_date,
    }
    r = requests.get(url, params)
    if r.json().get('totalItems') >0:
        game_date = r.json().get('dates')[0].get('date')
        home_team = r.json().get('dates')[0].get('games')[0].get('teams').get('home').get('team').get('id')
        away_team = r.json().get('dates')[0].get('games')[0].get('teams').get('away').get('team').get('id')
    else:
        home_team = 0,
        away_team = 0

    data = {
        'game_date': game_date,
        'home_team': home_team,
        'away_team': away_team,
    }

    return data


def get_games_for_date(sportId, game_date):
    url = 'http://statsapi.mlb.com/api/v1/schedule/games'
    params = {
        'sportId': sportId,
        'startDate': game_date,
        'endDate': game_date,
    }
    game = []
    r = requests.get(url, params)
    if r.json().get('totalItems') > 0:
        for g in range(r.json().get('totalItems')):
            game_time = datetime.strptime(r.json().get('dates')[0].get('games')[g].get('gameDate'),'%Y-%m-%dT%H:%M:%SZ').time()
            game.append({
                'game_time':  game_time,
                'home_team':  get_team(r.json().get('dates')[0].get('games')[g].get('teams').get('home').get('team').get('id')),
                'away_team':  get_team(r.json().get('dates')[0].get('games')[g].get('teams').get('away').get('team').get('id'))
            })
        data = game[:3]
    else:
        game = None
        data = game

    return data