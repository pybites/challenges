import pickle

from data import wattages, prices

CACHE = 'energy.data'

registered_devices = {}


class Cache:
    '''Context manager to cash results
    TODO: maybe convert in decorator ...'''

    def __enter__(self):
        try:
            self.cache = pickle.load(open(CACHE, "rb"))
        except FileNotFoundError:
            self.cache = {}
        return self.cache

    def __exit__(self, exc_type, exc_val, exc_tb):
        pickle.dump(self.cache, open(CACHE, "wb"))


class ApplianceCost:
    'Class to create appliance objects to track cost'

    def __init__(self, name, wattage, country, price_kwh):
        self.name = name
        self.wattage = int(wattage)
        self.country = country
        self.price_kwh = float(price_kwh)
        self._minutes = []  # log minutes

    @property
    def cost(self):
        'Show accumulated cost'
        hours_used = sum(self._minutes)/60
        cost = self.wattage * hours_used / 1000 * self.price_kwh
        return round(float(cost), 2)

    def consume(self, minutes):
        'Add number of minutes of consumption to device'
        if not isinstance(minutes, int):
            raise ValueError('Please use int for minutes')
        self._minutes.append(minutes)

    def __str__(self):
        return '{} ({}W/{}/{} kwh)\nConsumed: {} min / cost: {}\n'.format(
            self.name, self.wattage, self.country, self.price_kwh,
            sum(self._minutes), self.cost)


def _print_sequence(sequence):
    for i, item in sequence.items():
        print('{:<2}: {:<30}'.format(i, item[:28]), end='')
        if i % 3 == 0:
            print()
    print()


def _get_device():
    'Helper to let user choose device and get its wattage'
    devices = dict(enumerate(sorted(wattages), 1))
    _print_sequence(devices)
    while 1:
        try:
            dev_num = int(input('Choose device number: '))
        except ValueError:
            print('Please choose a number')
            continue
        if dev_num not in devices:
            print('Please choose a valid number')
            continue
        device = devices.get(dev_num)
        return device, wattages.get(device)


def _get_kwh_price():
    '''Helper to let user select country and get its kwh
    very similar to previous function, so best to abstract
    _get_wattage and _get_kwh_price in one function'''
    countries = dict(enumerate(sorted(prices), 1))
    _print_sequence(countries)
    while 1:
        try:
            co_num = int(input('Choose country number: '))
        except ValueError:
            print('Please choose a number')
            continue
        if co_num not in countries:
            print('Please choose a valid number')
            continue
        country = countries.get(co_num)
        price = prices.get(country)
        return country, price


def main():
    while 1:
        # TODO probably want to return one object (= make namedtuples)
        dev_name, wattage = _get_device()
        country, price = _get_kwh_price()
        key = (dev_name, country)
        try:
            device = registered_devices[key]
            print('found dev {} in cache, retrieving it'.format(dev_name))
        except KeyError:
            device = ApplianceCost(dev_name, wattage, country, price)

        try:
            minutes = int(input('Enter consumption entries (in minutes): '))
        except ValueError:
            print('Please enter an int for minutes')
            continue

        device.consume(minutes)
        # TODO add a decorator around this to cache results
        # = pickle registered_devices to file
        registered_devices[key] = device

        print('\nEnergy consumptions'.upper())
        for (dev, co), details in registered_devices.items():
            key = '{} - {}'.format(dev, co)
            print('{:*^80}'.format(key))
            print(details)

        cont = input('Continue? [yn] ')
        if cont.lower() == 'n':
            print('Bye')
            break


if __name__ == '__main__':
    main()
