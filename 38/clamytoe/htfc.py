import re
import sys
import requests


def parse_it(user, data):
	prs = []
	for event in data:
		try:
			date = event['payload']['pull_request']['created_at']
			type = event['type']
			if '2017-10' in date and type == 'PullRequestEvent':
				pr_user = event['payload']['pull_request']['head']['user']\
                          ['login']
				if pr_user == user:
					pr = []
					date = date.split('-')[2].split('T')[0]
					title = event['payload']['pull_request']['title']
					title += ' on October {}'.format(date)
					html_url = event['payload']['pull_request']['html_url']
					html_url = re.sub('https://github.com/', '', html_url)
					html_url = re.sub('/pull/', '#', html_url)
					pr.append(pr_user)
					pr.append(html_url)
					pr.append(title)
					prs.append(pr)
		except:
			pass
	return prs


def get_user(user):
	url = 'https://api.github.com/users/{}/events'.format(user)
	r = requests.get(url)
	return r.json()


def header():
	print('''.  .       ,    .        ._       , 
|__| _. _.-+- _ |_  _ ._.|, _  __-+-
|  |(_](_. | (_)[_)(/,[  | (/,_)  | 
		 __ .        .        
		/  `|_  _  _.;_/ _ ._.
		\__.[ )(/,(_.| \(/,[  
		                      
	''')


def show_reults(prs):
	messages = [
		"It's not too late to start!",
		'Off to a great start, keep going!', 
		'Half way there, keep it up!',
		'So close!',
		'Way to go!',
		"Now you're just showing off!"
	]
	pr_cnt = len(prs)
	print('\n{}/4'.format(pr_cnt))
	if pr_cnt == 0:
		print(messages[0])
		sys.exit()
	elif pr_cnt > 5:
		print(messages[5])
	else:
		print(messages[pr_cnt])
	
	for pr in prs:
		print('\n---\n{} submitted a pull request'.format(pr[0]))
		print(pr[1])
		print(pr[2])


def main():
	header()
	user = input("GitHub username: ")
	print('Searching for pull request...')
	data = get_user(user)
	pull_requests = parse_it(user, data)
	show_reults(pull_requests)


if __name__ == '__main__':
	main()

