import requests
import base64 as b64
import sqlite3
import os
import itertools as it

# Don't run this script too much or you get rate-limit blocked :(

FIRST_SET_TOTAL_TRANSCRIPTS = 79
SECOND_SET_START = 96
SECOND_SET_END = 187

"""
    Generator function that will yield the transcript number and transcript for every
    available transcript. This is done so that the strings don't take up too much memory
    all at once and slow down the script (subsequent operation of adding text to sqlite)
"""
def transcripts(url):
    for num in it.chain(range(0, FIRST_SET_TOTAL_TRANSCRIPTS + 1), 
                        range(SECOND_SET_START, SECOND_SET_END + 1)):
        # Creates file names going 000.txt, ...014.txt, ... 186.txt
        transcript_num = f'{num:0>3}.txt'
        headers = {'Authorization': f'token {os.environ.get("TPT_OAUTH_TOKEN")}'}
        result = requests.get(url + transcript_num, headers=headers)

        # Obtain the textual portion of the file
        data = result.json()['content']

        # Decode the base64 text content of the file
        transcript = b64.b64decode(data)
        yield transcript_num, transcript

""" Takes each transcript_num and transcript from the generator function above
    and stores it into an sqlite database """
def store_transcripts(filename, url):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    for transcript_num, transcript in transcripts(url):
        curs.execute(f"INSERT INTO transcripts VALUES (?,?)", (transcript_num, transcript))
        conn.commit()
    
    conn.close()

""" This function sets up an sqlite database. Only needs to be run if a sqlite db with
    the name 'filename' does not exist yet """
def set_up_db(filename):
    conn = sqlite3.connect(filename)
    curs = conn.cursor()
    curs.execute('CREATE TABLE transcripts (number text PRIMARY KEY, transcript text)')
    conn.commit()
    conn.close()

def main():
    url = 'https://api.github.com/repos/mikeckennedy/talk-python-transcripts/contents/transcripts/'
    
    sqlite_file = 'talk-python-transcripts.sqlite'

    set_up_db(sqlite_file)
    store_transcripts(sqlite_file, url)


if __name__ == '__main__':
    main()