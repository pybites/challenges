import praw
import json

def login_bot():
    with open('credentials.json') as creds:
        data = json.loads(creds.read())

    reddit = praw.Reddit(client_id=data['reddit_first_bot_client_id'],
                        client_secret=data['reddit_first_bot_client_secret'],
                        password=data['password'],
                        username=data['username'],
                        user_agent='My first reddit bot')
    
    if reddit.user.me() == data['username']:
        print("Success")
        return reddit
    else:
        exit()

def get_posts(reddit):
    # Retrieve some subreddits where we can post the generic 'NICE!'
    subreddit_names = ['mildlyinteresting','aww','Showerthoughts','me_irl','Jokes',
                       'interestingasfuck','PrequelMemes','NatureIsFuckingLit','oddlysatisfying',
                       'ProgrammerHumor']

    for subreddit_name in subreddit_names:

        subreddit = praw.models.Subreddit(reddit, subreddit_name)

        posts = subreddit.new()
        
        for post in posts:

            if post.score >= 400:

                yield post

def reply_nice(reddit):
    for post in get_posts(reddit):
        
        comments = post.comments

        repost = any('repost' in comment.body for comment in comments)

        if not repost:
            post.reply('NICE!')

def main():
    reddit = login_bot()
    # get_posts(reddit)
    reply_nice(reddit)

if __name__ == '__main__':
    main()