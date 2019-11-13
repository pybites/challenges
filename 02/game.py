from data import DICTIONARY, LETTER_SCORES, POUCH
from random import randint
from itertools import permutations

NUM_LETTERS = 7


def _get_permutations_draw(letters_):
    return [list(permutations(letters_, i)) for i in range(1, NUM_LETTERS + 1)]
    # return list(permutations(letters_))


def build_word(word_):
    word = []
    wrd = ''
    for c in word_:
        wrd += c
    #    for i in range(len(c)):
    #        word.append(c[i])
    #word2 = [c[i] for c in word_ for i in range(len(c))]

    return wrd.lower()  # ''.join(word).lower()


def get_possible_dict_words(letters_, dictionary_=DICTIONARY):
    all_words = _get_permutations_draw(letters_)
    dict_words = []

    # get dictionary words
    for words in all_words:
        for i in range(len(words)):
            word = build_word(words[i])

            if word in dictionary_ and word not in dict_words:
                dict_words.append(word)

    return dict_words


def _validation(word_, letters_):
    if not is_input_valid(letters_, word_):
        raise ValueError


def draw_letters():
    return [POUCH[randint(1, len(POUCH))] for i in range(NUM_LETTERS)]


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words_):
    """Calc the max value of a collection of words"""
    return max(words_, key=calc_word_value)


def is_input_valid(valid_letters_, usr_word_):
    if usr_word_ not in DICTIONARY:
        print(f'{usr_word_.upper()} is not a valid word.')
        return False

    usr_word = usr_word_.upper()
    for c in usr_word:
        if c not in valid_letters_:
            print("Unauthorized use of letter(s) not in the provided list")
            return False

    valid_dict = {}
    for letter in valid_letters_:
        valid_dict[letter] = 1 if letter not in valid_dict else valid_dict[letter] + 1

    usr_dict = {}
    for letter in usr_word:
        usr_dict[letter] = 1 if letter not in usr_dict else usr_dict[letter] + 1

    for letter in usr_dict:
        if usr_dict[letter] > valid_dict[letter]:
            print("Unauthorized use of letter(s) not in the provided list")
            return False

    return True


def main():
    usr_letters = draw_letters()

    possible_words = get_possible_dict_words(usr_letters, DICTIONARY)

    print(f"Letters drawn: {', '.join(usr_letters)}")

    while True:
        usr_word = input("Form a valid word: > ")
        usr_word = usr_word.strip().lower()

        if is_input_valid(usr_letters, usr_word):
            break  # Exit - valid word

    usr_value = calc_word_value(usr_word)
    best_word = max_word_value(possible_words)
    best_value = calc_word_value(best_word)

    usr_word = usr_word.upper()
    best_word = best_word.upper()

    if best_value == usr_value and best_word != usr_word:
        print(
            f'Your word {usr_word} (Value: {usr_value}), although very good, is not quite as nice as the best word {best_word}.')
        print(f'The best word: {best_word} (Value: {best_value})')
    elif best_value == usr_value and best_word == usr_word:
        print(f'Excellent, you found the best word: {best_word} (Value: {best_value})')
    else:
        print(f'Yor chosen word: {usr_word} (Value: {usr_value})')
        print(f'Best word: {best_word}. (Value: {best_value})')

    print(f'You scored: {((usr_value / best_value) * 100):.1f}')


if __name__ == "__main__":
    main()
