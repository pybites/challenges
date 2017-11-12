from bottle import request, route, run, static_file
import json
import urllib.request

statements = [
    'It\'s not too late to start!',
    'Off to a great start, keep going!',
    'Half way there, keep it up!',
    'So close!',
    'Way to go!',
    'Now you\'re just showing off!'
]

def get_events(uname):
	url = "https://api.github.com/search/issues?\
q=-label:invalid+created:2017-09-30T00:00:00-12:00..2017-10-31T23:59:59-12:00\
+type:pr+is:public+author:{}".format(uname)
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		result = json.loads(response.read().decode('utf-8'))
	return len(result['items'])


def message(uname):
	num_prs = get_events(uname)
	index = min(num_prs, 5)
	return "You have {} pull request(s). {}".format(index, statements[index])


@route('/')
def index():
	uname = request.query.get('username')
	if uname is not None:
		return message(uname)
	else:
		return static_file('index.html', root='./')

run(host='localhost', port=8080)