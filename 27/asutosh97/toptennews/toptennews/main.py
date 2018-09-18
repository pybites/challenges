#!/usr/bin/python
import praw
import urllib2
import config

# Checks for an active internet connection
def internet_active():
	print("Checking for an active internet connection...")
	try:
		response = urllib2.urlopen('http://www.google.com', timeout=20)
		print("Internet connection verified...")
		return True
	except urllib2.URLError as err:
		print("No active internet connection...")
		return False

# logs in bot
def bot_login():
	print("Logging in...")
	bot_handle = praw.Reddit(
						username = config.username,
						password = config.password,
						client_id = config.client_id,
						client_secret = config.client_secret,
						user_agent = "fetches weekly programming challenges"
						)
	print("Login Successful!!!")
	return bot_handle

def get_hot_news(bot_handle, limit):
	print("Fetching News...")
	return sorted(bot_handle.subreddit("news").hot(limit = limit), key = lambda x: x.score, reverse = True)

def print_news(news):
	for item in news:
		print("Title: ", item.title)
		print("Score: ", item.score)
		print("---------------------------------\n")

def main():
	if internet_active():
		bot_handle = bot_login()
		news = get_hot_news(bot_handle, limit = 10)
		print_news(news)

if __name__ == "__main__":
	main()
