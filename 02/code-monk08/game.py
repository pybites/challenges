import itertools
import random
from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    random.shuffle(POUCH)
    return random.choices(POUCH, k=NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    while True:
        print(f"valid word contains the letters which are in the sequence draw: {draw} and word should be in the dictionary ")
        enteredword = input('enter the valid word ').upper()
        if _validation(enteredword, draw):
            return enteredword
        raise ValueError


def _validation(word, draw):
    """1) Only use letters of draw
    2)valid dictionary word"""
    for char in word:
        if char.upper() not in draw:
            return False
    if word.upper() not in DICTIONARY:
        return False
    return True


def calc_word_value(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    answer = _get_permutations_draw(draw)
    for word in answer:
        if word not in DICTIONARY:
            answer.remove(word)
    return answer


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    answer = []
    for n in range(1, NUM_LETTERS+1):
        possible_words = ["".join(groups) for groups in list(
            itertools.permutations(draw, n))]
        answer.extend(possible_words)
    return answer


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == '__main__':
    main()
