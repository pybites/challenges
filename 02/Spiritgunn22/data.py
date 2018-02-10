from collections import namedtuple

Letter = namedtuple('Letter', 'name amount value')

def _load_words():
    with open('dictionary.txt') as f:
        return set([word.strip().lower() for word in f.read().split()])

DICTIONARY = _load_words()
assert len(DICTIONARY) == 234371


# generated with https://github.com/pybites/blog_code/blob/master/BeautifulSoup/scrabble_distribution.py
distribution = [Letter(name='A', amount='9', value='1'), Letter(name='B', amount='2', value='3'), Letter(name='C', amount='2', value='3'), Letter(name='D', amount='4', value='2'), Letter(name='E', amount='12', value='1'), Letter(name='F', amount='2', value='4'), Letter(name='G', amount='3', value='2'), Letter(name='H', amount='2', value='4'), Letter(name='I', amount='9', value='1'), Letter(name='J', amount='1', value='8'), Letter(name='K', amount='1', value='5'), Letter(name='L', amount='4', value='1'), Letter(name='M', amount='2', value='3'), Letter(name='N', amount='6', value='1'), Letter(name='O', amount='8', value='1'), Letter(name='P', amount='2', value='3'), Letter(name='Q', amount='1', value='10'), Letter(name='R', amount='6', value='1'), Letter(name='S', amount='4', value='1'), Letter(name='T', amount='6', value='1'), Letter(name='U', amount='4', value='1'), Letter(name='V', amount='2', value='4'), Letter(name='W', amount='2', value='4'), Letter(name='X', amount='1', value='8'), Letter(name='Y', amount='2', value='4'), Letter(name='Z', amount='1', value='10')]

POUCH = list(''.join(
        list(letter.name * int(letter.amount) 
            for letter in distribution))
    )
assert len(POUCH) == 98  # no wildcards in this simple game


LETTER_SCORES = dict(zip(
        [letter.name for letter in distribution],
        [int(letter.value) for letter in distribution]
    ))

assert LETTER_SCORES['A'] == 1
assert LETTER_SCORES['Q'] == 10
assert sum(LETTER_SCORES.values()) == 87
