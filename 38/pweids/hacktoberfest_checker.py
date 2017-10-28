from bottle import request, route, run, static_file
import requests

statements = [
    'It\'s not too late to start!',
    'Off to a great start, keep going!',
    'Half way there, keep it up!',
    'So close!',
    'Way to go!',
    'Now you\'re just showing off!'
]

def get_events(uname):
	url = "https://api.github.com/users/{}/events".format(uname)
	req = requests.get(url)
	return r.json()


def message(uname):
	json = get_events(uname)
	

@route('/')
def index():
	uname = request.query.get('username')
	if uname is not None:
		return message(uname)
	else:
		return static_file('index.html', root='./')

run(host='localhost', port=8080)