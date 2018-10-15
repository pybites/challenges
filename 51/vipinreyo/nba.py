from collections import namedtuple
import csv
import os
import sqlite3

import requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
DATA_CACHED = 'nba.data'
NBA_DB = 'nba.db'

# start clean
if os.path.isfile(NBA_DB):
    os.remove(NBA_DB)

Player = namedtuple('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(NBA_DB)
cur = conn.cursor()


def _get_csv_data():
    """GIVEN:
       Load in CSV data in from remote URL or local cache file"""
    if os.path.isfile(DATA_CACHED):
        with open(DATA_CACHED) as f:
            return f.read()
    else:
        with requests.Session() as session:
            return session.get(DATA_URL).content.decode('utf-8')


def load_data():
    """GIVEN:
       Converts NBA CSV data into a list of Player namedtuples"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        player = Player(name=row['Player'],
                        year=row['Draft_Yr'],
                        first_year=row['first_year'],
                        team=row['Team'],
                        college=row['College'],
                        active=row['Yrs'],
                        games=row['Games'],
                        avg_min=row['Minutes.per.Game'],
                        avg_points=row['Points.per.Game'])
        yield player


# CODE HERE (tests under __main__):

def import_to_db(players=None):
    """Create database table in sqlite3 and import the players data

       required table SQL:
       CREATE TABLE players (name, year, first_year, team, college,
                             active, games, avg_min, avg_points)
    """
    if players is None:
        players = list(load_data())

    # Create the table db statement
    players_table = """CREATE TABLE players (
                            name text,
                            year integer,
                            first_year integer,
                            team text,
                            college text,
                            active integer,
                            games integer,
                            avg_min real,
                            avg_points real
                            ); """

    cur.execute(players_table)

    # Insert players to the table
    with conn:
        cur.executemany("insert into players (name, year, first_year, team, college, active, games,"
                            " avg_min, avg_points) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", players)


def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    sql = ''' select name from players group by games order by avg_points desc limit 1;'''
    cur.execute(sql)
    result = cur.fetchall()
    return result[0][0]


def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    sql = '''select count(*) from players where college == 'Duke University';'''
    cur.execute(sql)
    result = cur.fetchall()
    return result[0][0]


def percentage_of_players_first_year():
    """Return 2 digit percentage of players whose first year it is
       (first_year column)"""
    sql1 = '''select count(*) from players where first_year == 1'''
    sql2 = '''select count(*) from players'''
    cur.execute(sql1)
    count_players_first_year = cur.fetchall()[0][0]
    cur.execute(sql2)
    count_players = cur.fetchall()[0][0]
    return (count_players_first_year/count_players) * 100


def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    sql = '''select avg(active) from players where college == 'Stanford University';'''
    cur.execute(sql)
    result = cur.fetchall()
    return result[0][0]


def year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    sql = '''select year, count(*) as cnt from players group by year order by cnt desc limit 1;'''
    cur.execute(sql)
    result = cur.fetchall()
    return result[0][0]


def most_games_per_year_for_veterans():
    """Top 6 players that are > 10 years active, that have the
       highest # games / year"""
    sql = '''select name, max(games/active) as games_per_year from players where active > 10
              group by year order by games_per_year desc limit 6;'''
    cur.execute(sql)
    result = cur.fetchall()
    return [data[0] for data in result]


if __name__ == '__main__':
    import_to_db()

    # A. check if the import went well
    def _verify_total_row_count_after_import():
        sql = '''SELECT COUNT(*) FROM players'''
        cur.execute(sql)
        ret = cur.fetchall()
        return ret[0][0]

    assert _verify_total_row_count_after_import() == 3961

    # B. some simple asserts of the data analysis functions
    assert player_with_max_points_per_game() == 'Michael Jordan'

    assert number_of_players_from_duke() == 58

    assert round(avg_years_active_players_stanford(), 2) == 4.58

    assert round(percentage_of_players_first_year(), 2) == 1.51

    assert int(year_with_most_drafts()) == 1984

    expected = ['A.C. Green', 'Alex English', 'Jack Sikma',
                'John Stockton', 'Mark Eaton', 'Terry Tyler']
    assert sorted(most_games_per_year_for_veterans()) == expected
