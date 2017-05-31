import console
import decimal
import ui

from sys import exit

def watt_hours(watts, hours):
	return watts * hours
	
def kilowatt_hours(watt_hrs):
	return watt_hrs / 1000

def watts_over_time(k_hours, days):
	return k_hours * days

def calc_cost(kWh, cost):
	return kWh * cost

def how_much(sender):
	'@type sender: ui.Button'
	# watts, cost, hours, days
	D = decimal.Decimal
	cent = D('0.01')
	
	w_field = sender.superview['w_field']
	h_field = sender.superview['h_field']
	c_field = sender.superview['c_field']
	results = sender.superview['results']
	t_label = sender.superview['total']
	button = sender.superview['button']
	
	try:
		watts = int(w_field.text)
	except ValueError as e:
		alert_result = console.alert('Watts Error', 'Watts must be a whole number', 'OK')
		exit()
	
	try:
		hours = int(h_field.text)
	except ValueError as e:
		alert_result = console.alert('Hours Error', 'Hours must be a whole number', 'OK')
		exit()
	
	try:
		cost = float(c_field.text)
	except ValueError as e:
		alert_result = console.alert('Cost Error', 'Cost must be a floating point number', 'OK')
		exit()
	
	days = 30
	
	watt_hrs = watt_hours(watts, hours)
	w_hour = kilowatt_hours(watt_hours(watts, 1))
	k_hours = kilowatt_hours(watt_hrs)
	kWh = watts_over_time(k_hours, days)
	total = calc_cost(kWh, cost)
	
	total_decimal = D(str(total))
	total_cost = total_decimal.quantize(cent, rounding=decimal.ROUND_UP)
	
	results.text = '{} kWh per hour\n{} kWh per day\n{} kWh per month'.format(w_hour, k_hours, kWh)
	t_label.text = '${}'.format(total_cost)

def main():
	v = ui.load_view('wattage')
	v.present(orientations=['portrait'])

if __name__ == '__main__':
	main()

