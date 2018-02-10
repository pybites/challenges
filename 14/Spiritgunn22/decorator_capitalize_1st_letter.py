from functools import wraps
import random


def upper_first_letter(func):
    '''Decorator that uppercases the first letter of the
     word returned by func'''
    @wraps(func)  # preserves function meta data
    def wrapper():
        word = func()
        letter = word[0].upper()
        return letter + word[1:]
    return wrapper


@upper_first_letter
def get_word():
    '''returns one of the 1st 10 greek letters of the alphabet at random'''
    word_list = ['alpha', 'beta', 'gamma', 'delta', 'epsilon',
                 'eta', 'zeta', 'theta', 'iota', 'kappa']
    return word_list[random.randint(0, 9)]


if __name__ == '__main__':
    print(get_word())
