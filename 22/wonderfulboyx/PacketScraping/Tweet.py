import twitter
import configparser


class Tweet(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("setting.ini")
        self.api = twitter.Api(consumer_key=config['Tweet']['consumer_key'],
                               consumer_secret=config['Tweet']['consumer_secret'],
                               access_token_key=config['Tweet']['access_token_key'],
                               access_token_secret=config['Tweet']['access_token_secret'],)

    def Post(self, message):
        self.api.PostUpdate(message)
