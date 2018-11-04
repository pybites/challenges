from request_db import request_db
from tabulate import tabulate


def data_parsing(data_list):
    if not data_list:
        print('Incorrect AS number')
    else:
        i = 1
        for diction in data_list:
            if diction['name'] == 'route' or diction['name'] == 'route6':
                if i == 0:
                    descr.append('')
                route.append(diction["value"])
                i = 0
            elif diction['name'] == 'descr':
                descr.append(diction["value"])
                i = 1
        if len(descr) < len(route):
            descr.append('')
    data_tup = tuple(zip(route, descr))
    return data_tup


descr = []
route = []
columns = ['Route', 'Description']
data = request_db()
pars_data = data_parsing(data)
print(tabulate(pars_data, headers=columns, tablefmt="grid"))