# game.py - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html


from data import DICTIONARY, LETTER_SCORES, POUCH
from random import choices
from itertools import permutations, chain

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters():
    return choices(POUCH, k=NUM_LETTERS)


def _validation(word, draw):
    # verify all letters from word are in draw and all letters in draw are used only once
    draw_ = draw.copy()
    for c in word.upper():
        if c in draw_:
            draw_.remove(c)
        else:
            raise ValueError(f'The letter {c} is used too much')
    # verify word is in the dictionary
    if word.lower() not in DICTIONARY:
        raise ValueError(f'{word} is not a valid word')
    return True


def _get_permutations_draw(draw):
    perms = []
    for r in range(1, NUM_LETTERS + 1):
        perms.extend(permutations(draw, r=r))
    return [''.join(perm) for perm in perms]


def get_possible_dict_words(draw):
    return [combo for combo in _get_permutations_draw(draw) if combo.lower() in DICTIONARY]


def get_optimal_word(draw):
    return max_word_value(get_possible_dict_words(draw))


def main():
    print(f'Letters drawn: {", ".join(draw := draw_letters())}')
    user_input = input('Form a valid word: ')
    if _validation(user_input, draw):
        print(f'Word chosen: {user_input.upper()} (value: {calc_word_value(user_input)})')
        optimal = get_optimal_word(draw)
        print(f'Optimal word possible: {optimal} (value: {calc_word_value(optimal)})')
        print(f'You scored: {round(calc_word_value(user_input) / calc_word_value(optimal) * 100, 1)}')


if __name__ == "__main__":
    # print(DICTIONARY)
    # for _ in range(100):
    #     print(draw_letters())
    # print(d := draw_letters())
    # print(_get_permutations_draw(d))
    # print(get_possible_dict_words(d))
    # print(o := get_optimal_word(d), calc_word_value(o))
    main()
