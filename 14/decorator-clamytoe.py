from getpass import getpass
from functools import wraps
from os import system

from passlib.hash import pbkdf2_sha512

def hashit(func):
    """Decorator to securely hash passwords"""

    @wraps(func)  # preserves function meta data
    def wrapper():
        # hash the password
        return pbkdf2_sha512.hash(func())

    return wrapper


def boxit(func):
    """Decorator to draw a box around text"""
    # size of the padding to use
    pad = 4

    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        title = func(*args, **kwargs)
        title_len = len(title)

        # custom padding depending on length of title
        if title_len % 2 == 0:
            title_len += pad * 2
            padding_l = pad
            padding_r = pad
        else:
            title_len += pad * 2 + 2
            padding_l = pad
            padding_r = pad

        # create each section
        box_horizontal = '#' * title_len
        box_left = '#' + ' ' * padding_l
        box_right = ' ' * padding_r + '#'

        # assemble the title with box around it
        boxed = box_horizontal + '\n'
        boxed += box_left + title + box_right + '\n'
        boxed += box_horizontal

        return boxed

    return wrapper


@boxit
def draw_title(title):
    """Returns some text after clearing the console"""
    system('cls||clear')

    return title


@hashit
def get_passwd():
    """Asks for a password and then returns it"""
    passwd = getpass("Enter your password: ")

    return passwd


def confirm_passwd():
    """Password hasing verification"""
    hashed_passwd = get_passwd()
    # uncomment next line to see hashed password
    # print("Hashed password: {}".format(hashed_passwd))
    clear_passwd = getpass("Verify your password: ")

    # verify that the passwords match
    verify = pbkdf2_sha512.verify(clear_passwd, hashed_passwd)

    print("Passwords match!" if verify else "Passwords do not match!")


if __name__ == '__main__':
    print(draw_title('Verification Demo'))
    confirm_passwd()
