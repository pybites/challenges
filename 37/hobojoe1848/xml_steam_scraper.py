#!python3
# steam_scraper.py is a simple web scraper to check for the latest steam games

from collections import namedtuple
import requests
import sqlite3

import feedparser

FEED_FILE = "newreleases.xml"
DB_NAME = "steam_games.db"
Game = namedtuple('Game', 'title url')


def check_create_db():
    with sqlite3.connect(DB_NAME) as connection:
        c = connection.cursor()
        try:
            c.execute("""CREATE TABLE new_steam_games
                    (Name TEXT, Link TEXT, Emailed TEXT)
                    """)		
        except:
            pass

			
def pull_db_data():
    db_games_list = []
    with sqlite3.connect(DB_NAME) as connection:
        c = connection.cursor()
        c.execute("SELECT Name from new_steam_games")
        db_games_list = c.fetchall()
        return db_games_list

        
def parse_that_feed_baby():
    feed_list = []
    feed = feedparser.parse(FEED_FILE)
    for entry in feed['entries']:
        game_data = Game(title=entry['title'], url=entry['link'])
        feed_list.append(game_data)
    return feed_list


def check_for_new(feed_list, db_games):
    new_games_list = []
    for data in feed_list:
        if (data.title,) not in db_games:
            new_games_list.append(data)
    return new_games_list


def main():
    check_create_db()
    db_games = pull_db_data()
    new_games = check_for_new(parse_that_feed_baby(), db_games)
	
    with sqlite3.connect(DB_NAME) as connection:
        c = connection.cursor()
        c.executemany("INSERT INTO new_steam_games VALUES (?, ?, 0)", new_games)	

if __name__ == "__main__":
    main()
