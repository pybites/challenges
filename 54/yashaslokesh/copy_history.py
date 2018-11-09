from datetime import datetime
from time import sleep

import pyperclip

''' pyperclip.copy() is queried every x seconds while script is running,
    and checks if the string is already in the log. If it is not, it is added
    as a new entry. If it is already in the log, a new datetime string will be added.
    All copied strings are stored in copy_history.txt, can be changed here
'''

LOG_FILE = 'copy_history.txt'

def load_file_contents():
    try:
        with open(LOG_FILE) as f: # Get list of all lines for easy insertion
            file_lines = f.read().splitlines()
    except FileNotFoundError: # If file doesn't exist, start with empty list
        file_lines = []

    return file_lines


def save_file_contents(file_lines):
    try: # If file does not exist, open it and write. Otherwise, overwrite the other file
        with open(LOG_FILE, 'x') as f:
            f.write('\n'.join(file_lines) + '\n')
    except FileExistsError:
        with open(LOG_FILE, 'w') as f:
            f.write('\n'.join(file_lines) + '\n')


def clipboard_watcher(time):
    ''' After a time second delay, starts recording clipboard every time seconds
    '''
    lines = load_file_contents()

    while True:
        try:
            sleep(time)
            copy = '\"' + pyperclip.paste() + '\"'
            print(f'\nPasted: {copy}\n')
            today = datetime.now().strftime("Copied: %B %d, %Y at %I:%M:%S %p")
            if copy in lines: # Inserts datetime.now() before the copied string
                lines.insert(lines.index(copy), today)
            else: # Adds everything to the end if the copied string is new
                lines.extend([today, copy, ''])
        except KeyboardInterrupt:
            save_file_contents(lines)
            exit()


def main():
    print('Enter the delay you want in between each scan of your clipboard.')
    print('After each delay, the clipboard will be queried again. ')
    time = int(input())
    clipboard_watcher(time)

if __name__ == '__main__':
    main()