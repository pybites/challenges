"""Top Topic Submissions Display

This script receives a subreddit topic and and displays the top topics submitted in
relation to the topic given
"""
import os
import praw
import prawcore

from dotenv import load_dotenv

load_dotenv()


def config_auth():
    """Return configuration settings"""
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
    )
    return reddit


def get_subreddit_topic():
    """Return subreddit topic."""
    while True:
        subreddit_topic = input("Enter Subreddit topic without quotes - ")
        try:
            if not subreddit_topic:
                continue
        except ValueError:
            print("Please enter an appropriate value/ Directory path!")
        else:
            return subreddit_topic


def display_top_topic_submission():
    """Display top submissions per given redit topic"""
    subreddit_topic = get_subreddit_topic()
    try:
        for submission in config_auth().subreddit(subreddit_topic).hot(limit=20):
            print(
                "-------------------------------------------------------------------------"
                "---------------------------------------------------------"
            )
            print("Topic Title: " + submission.title)
            print("Topic Link: " + submission.url)
            print("Topic Ups: " + str(submission.ups))
            print(
                "-------------------------------------------------------------------------"
                "---------------------------------------------------------"
            )
    except prawcore.exceptions.NotFound:
        print("Use a valid reddit subtopic. i.e learnpython, learnjava, etc")
    except prawcore.exceptions.Redirect:
        print("Use a valid reddit subtopic. i.e learnpython, learnjava, etc")


if __name__ == "__main__":
    display_top_topic_submission()
