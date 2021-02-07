import requests


def get_team_division(sportId, teamId):
    url = 'http://statsapi.mlb.com/api/v1/teams'
    params = {
        'sportId': sportId,
        'teamId': teamId,
    }
    r = requests.get(url, params)
    division = r.json().get('teams')[0].get('division').get('id')
    return division


def get_division_details(sportId, user_id):
    url = 'http://statsapi.mlb.com/api/v1/divisions'
    params = {
        'sportId': sportId
    }
    r = requests.get(url, params)
    divisions = []
    div_json = r.json().get('divisions')
    for d in div_json:
        default_division = False
        division_id = d.get('id')
        division_name = d.get('nameShort')
        if user_id:
            if division_id == 203:
                default_division = True
        else:
            default_division = get_team_division(sportId, 138)
        data = {
            'division_id': division_id,
            'division_name': division_name,
            'default_division': default_division
        }
        divisions.append(data)
        divisions = sorted(divisions, key=lambda division: (division['division_name']))
    return divisions


def get_leagues():
    """
    :return: list of leagues in the sort order specified by the MlB API
    """
    url = 'http://statsapi.mlb.com/api/v1/sports/'
    r = requests.get(url)
    leagues = r.json().get('sports')
    leagues = sorted(leagues, key = lambda team: (team['sortOrder']))
    league_display = []
    for i in range(len(leagues)):
        league_display.append({'id': leagues[i].get('id'), 'name': leagues[i].get('name')})
    return league_display

