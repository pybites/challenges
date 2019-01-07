import json
import requests


def request_as_prefixes(AS):
    prefix_r = requests.get(f'https://rest.db.ripe.net/search.json?inverse-attribute=origin&source=ripe&query-string'
                            f'=AS{AS}&types=route')
    prefix_r.raise_for_status()
    data = json.loads(prefix_r.text)
    data_list = [row_at for row in data['objects']['object'] for row_at in row['attributes']['attribute']]
    common_data_list = [diction for diction in data_list if diction['name'] == 'route' or diction['name'] == 'route6'
                 or diction['name'] == 'descr']
    return common_data_list


def request_as_neighbor(AS):
    as_neighbor_r = requests.get(f'https://stat.ripe.net/data/asn-neighbours/data.json?resource={AS}')
    as_neighbor_r.raise_for_status()
    data = as_neighbor_r.json()
    as_neighbor = data['data']['neighbour_counts']
    return as_neighbor
