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

def get_new_posts_of(bot_handle, sub_reddit_name, postCount):
	subreddit = bot_handle.subreddit(sub_reddit_name)
	return subreddit.new(limit = postCount)

def get_challenges_in_top(bot_handle, search_limit):
	easy, interm, hard = {}, {}, {}
	#while not easy and interm and hard:
	for post in get_new_posts_of(bot_handle, "dailyprogrammer", search_limit):
		if "[Easy]" in post.title:
			easy = post
		elif "[Intermediate]" in post.title:
			interm = post
		elif "[Hard]" in post.title:
			hard = post
		if easy and interm and hard:
			break
	return easy, interm, hard

def get_challenges(bot_handle):
	print("Fetching Challenges...")
	easy, med, hard = {}, {}, {}
	search_limit = 3
	while (not (easy and med and hard)):
		easy, med, hard = get_challenges_in_top(bot_handle, search_limit)
		search_limit = 2 * search_limit
	return easy, med, hard

# prints challenges in the console
def print_challenges(easy, interm, hard):
	print("\nEASY")
	print("Title: ", easy.title)
	print("---------------------------------")

	print("\nINTERMEDIATE")
	print("Title: ", interm.title)
	print("---------------------------------")

	print("\nHARD")
	print("Title: ", hard.title)
	print("---------------------------------\n")

def main():
	if internet_active():
		bot_handle = bot_login()
		easy, med, hard = get_challenges(bot_handle)
		print_challenges(easy, med, hard)


if __name__ == "__main__":
	main()
