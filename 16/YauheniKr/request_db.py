import json
import requests

def request_db():
    AS = input('Please, insert AS number: ')
    req = requests.get('http://rest.db.ripe.net/search.json?inverse-attribute=origin&source=ripe&query-string=AS' + AS +
                       '&types=route')
    data = json.loads(req.text)
    if 'errormessages' in data:
        return False
    else:
        data_list = [row_at for row in data['objects']['object']
                     for row_at in row['attributes']['attribute']]
        return data_list