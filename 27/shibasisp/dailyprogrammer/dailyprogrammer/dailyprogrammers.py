#! /usr/bin/env python
import praw
import config
import urllib2


def bot_login():
    """Login method."""
    print("logging in..")
    r = praw.Reddit(
                    username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Daily programmers challenge fetcher"
                   )
    print("Logged in!!")
    return r


def run_bot(r):
    print("Obtaining challenges...")
    subreddit = r.subreddit("dailyprogrammer")
    for submission in subreddit.new():
        if '[Easy]' in submission.title and not easy:
            easy.append({'title': submission.title,
                         'text': submission.selftext})
        elif '[Intermediate]' in submission.title and not medium:
            medium.append({'title': submission.title,
                           'text': submission.selftext})
        elif '[Hard]' in submission.title and not hard:
            hard.append({'title': submission.title,
                         'text': submission.selftext})


def print_challenges():
    print("\t1: Easy Challenge")
    print("\t2: Intermediate Challenge")
    print("\t3: Hard Challenge")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        print('==================================\n')
        print(easy[0]['title'])
        print('==================================\n')
        print(easy[0]['text'])
    elif choice == 2:
        print('==================================\n')
        print(medium[0]['title'])
        print('==================================\n')
        print(medium[0]['text'])
    elif choice == 3:
        print('==================================\n')
        print(medium[0]['title'])
        print('==================================\n')
        print(medium[0]['text'])
    else:
        print("\nWrong Choice! Try again(press \"Ctrl+C\" to terminate\n)")
        print_challenges()


def internet_on():
    """Check Internet connection."""
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError:
        return False

        
easy, medium, hard = [], [], []


def main():
    check_internet = internet_on()
    if check_internet:
        r = bot_login()
        run_bot(r)
        print_challenges()
    else:
        print("No Internet connection detected!")


if __name__ == "__main__":
    main()
