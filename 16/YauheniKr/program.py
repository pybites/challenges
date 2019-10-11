from request_db import request_as_prefixes, request_as_neighbor
from tabulate import tabulate


def as_prefixes(AS):
    descr = []
    route = []
    list_prefix_data = request_as_prefixes(AS)
    i = 1
    for diction in list_prefix_data:
        if (diction['name'] == 'route' or diction['name'] == 'route6') and i == 0:
            descr.append('')
            route.append(diction["value"])
            i = 0
        elif diction['name'] == 'descr':
            descr.append(diction["value"])
            i = 1
        elif (diction['name'] == 'route' or diction['name'] == 'route6') and i == 1:
            route.append(diction["value"])
            i = 0
    if len(descr) < len(route):
        descr.append('')
    prefix_tuple = tuple(zip(range(1, len(route)+1), route, descr))
    return prefix_tuple


def as_neighbor(AS):
    dict_data_neighbor = request_as_neighbor(AS)
    return dict_data_neighbor


def main():
    columns = ['№', 'Route', 'Description']
    AS = input('Please, insert AS number: ')
    print()
    print(f'AS has {as_neighbor(AS)["left"]} uplink AS and has {as_neighbor(AS)["right"]} downlink clients AS')
    print()
    print(f'AS has {len(as_prefixes(AS))} public prefixes registered')
    print()
    print(tabulate(as_prefixes(AS), headers=columns, tablefmt="grid"))


if __name__ == '__main__':
    main()
