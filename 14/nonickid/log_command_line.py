from functools import wraps
from getpass import getpass

username = None
password = None

def logcommand(func):
    '''Decorator to ...'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        # do stuff before func
        cmd = func(*args, **kwargs)
        # do stuff after func
        if len(cmd) > 0:
           print(f"Command '{cmd}' executed by {username} has been logged")
        return cmd
    return wrapper


@logcommand
def prompt_line(prompt_fmt='> '):
    cmd = input(prompt_fmt)
    return cmd

def command_line():
    while True:
        cmd = prompt_line('prompt> ')
        if cmd == 'exit':
            break

def log_in():
    username = input('Username: ')
    password = getpass('Password: ')
    print(f'Welcome {username}!')
    command_line()

if __name__ == '__main__':
    log_in()
