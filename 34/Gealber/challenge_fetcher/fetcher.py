import requests
from bs4 import BeautifulSoup
import sqlite3

BASE_URL = "https://codechalleng.es"

def insert_data(store: list):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('DELETE FROM api_challenge')
    cur.executemany('INSERT INTO api_challenge VALUES (?,?,?)', store)
    conn.commit()
    conn.close()

def main():
    r = requests.get(BASE_URL+'/challenges/')
    home_page = r.content
    soup = BeautifulSoup(home_page, "lxml")
    challenges_links = soup.select("#filterList2 > tbody > tr > td > a")
    length = len(challenges_links)
    store = [(length-i, "".join([BASE_URL,el.get("href")]), el.text) for i, el in enumerate(challenges_links)]
    insert_data(store)

if __name__ == "__main__":
    main()
