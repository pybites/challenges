import console
import decimal
import ui

from sys import exit


def watt_hours(watts, hours):
    """Multiplies watts times the hours used"""
    return watts * hours


def kilowatt_hours(watt_hrs):
    """"Divides watts per hour by 1000 to convert to kWh"""
    return watt_hrs / 1000


def watts_over_time(k_hours, days):
    """Calculates kilowatt hours used over the days specified"""
    return k_hours * days


def calc_cost(kWh, cost):
    """Calculates the cost of the kilowatts based on the cost provided"""
    return kWh * cost


def how_much(sender):
    """Receives input from user and does the calculations"""
    '@type sender: ui.Button'
    # using decimal to get more accurate monetary calculations
    D = decimal.Decimal
    cent = D('0.01')

    # populate local variables from the ui elements
    w_field = sender.superview['w_field']
    h_field = sender.superview['h_field']
    c_field = sender.superview['c_field']
    results = sender.superview['results']
    t_label = sender.superview['total']
    # button = sender.superview['button']

    # Try an catch some obvious entries
    try:
        watts = int(w_field.text)
    except ValueError as e:
        message = 'Watts must be a whole number'
        alert_result = console.alert('Watts Error', message, 'OK')
        exit()

    try:
        hours = int(h_field.text)
    except ValueError as e:
        message = 'Hours must be a whole number'
        alert_result = console.alert('Hours Error', message, 'OK')
        exit()

    try:
        cost = float(c_field.text)
    except ValueError as e:
        message = 'Cost must be a floating point number'
        alert_result = console.alert('Cost Error', message, 'OK')
        exit()

    # setting number of days per month to 30
    days = 30

    # calling functions to generate the calculations
    watt_hrs = watt_hours(watts, hours)
    w_hour = kilowatt_hours(watt_hours(watts, 1))
    k_hours = kilowatt_hours(watt_hrs)
    kWh = watts_over_time(k_hours, days)
    total = calc_cost(kWh, cost)

    # using the decimal object for proper rounding
    total_decimal = D(str(total))
    total_cost = total_decimal.quantize(cent, rounding=decimal.ROUND_UP)

    # return results to the screen
    results.text = f'{w_hour:.3f} kWh per hour\n'\
                   f'{k_hours:.2f} kWh per day\n'\
                   f'{kWh:.2f} kWh per month'
    t_label.text = f'${total_cost}'


def main():
    # load the ui view and set to protrait mode
    v = ui.load_view('wattage')
    v.present(orientations=['portrait'])


if __name__ == '__main__':
    main()
