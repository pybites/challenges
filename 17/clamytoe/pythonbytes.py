# http://pybit.es/codechallenge17.html
# quick template (instructions converted into methods)
# could use class as well
# use as needed (not required of course)
#
from time import sleep

INTERVAL = 24 * 60 * 60  # change if you don't want every day
FEED = 'https://pythonbytes.fm/episodes/rss'

# Send out new episode and mark as complete


def main():
    while True:
        feed = parse_feed()
        for episode in feed:
            pass
        # ...
        # etc
        # ...
        sleep(INTERVAL)  # or use system cron / sched / pypi


if __name__ == '__main__':
    main()
