from pprint import pprint
from subprocess import Popen, PIPE
import re

import requests

from api_key import key

def return_city_state(ip):
    url = f'http://api.ipstack.com/{ip}?access_key={key}'
    r = requests.get(url)
    data = r.json()
    return ip, data['city'], data['region_name'], data['country_name']


def get_ips_from_tracert(url):
    ips = []
    p = Popen(['tracert', url], stdout=PIPE)
    while True:
        line = p.stdout.readline().decode("utf-8", "strict")
        ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if ip:
            ips.append(ip.group(0))
        if not line:
            break
    return ips[1:]


if __name__ == '__main__':
    urls = [
        'www.google.com',
        'www.ufl.edu',
        'www.wikileaks.org',
        'www.codechalleng.es',
        'www.talkpython.fm'
    ]

    for url in urls:
        print()
        print(f'Searching ip address trace for {url}')
        ips = get_ips_from_tracert(url)
        for ip in ips:
            print(return_city_state(ip))

    # while True:
    #     print()
    #     search = input('what url do you want to trace? (q to quit) ')
    #     if search == 'q':
    #         quit()
    #     ips = get_ips_from_tracert(search)

    #     for ip in ips:
    #         print(return_city_state(ip))
