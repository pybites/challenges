from secrets import choice
from itertools import permutations
from data import DICTIONARY, POUCH

NUM_LETTERS = 7


class Draw(object):
    def __init__(self, pouch=POUCH):
        self.pouch = POUCH
        # keep track of iterations
        self._index = 0
        self.draw = Draw.draw_letters(self)

    def __call__(self):
        # if not self.draw:
        #     self.draw = self.draw_letters()
        return self.draw

    def __str__(self):
        return ", ".join(self.draw)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.draw):
            # each time called return last element of list
            result = self.draw[self._index]
            # increment so we eventual stop
            self._index += 1
            return result
        else:
            self._index = 0
            raise StopIteration

    @staticmethod
    def draw_letters(self, count=NUM_LETTERS):
        drawn_letters = []
        # for all 7 letters randomly choice from POUCH,
        # remove from pouch and append to drawn_letters
        for n in range(count):
            letter = choice(self.pouch)
            self.pouch.remove(letter)
            drawn_letters.append(letter)
        return drawn_letters

    def get_possible_dict_words(self, draw=[]):
        """Get all possible words from draw which are valid dictionary words.
        Use the _get_permutations_draw helper and DICTIONARY constant
        params:
            draw: list
        if draw is not supplied use self.draw
        """
        # return filter(lambda word: _is_valid_word(word, self.draw), DICTIONARY)
        if not draw:
            draw = self.draw

        perms = self._get_permutations_draw(draw)
        possible = []
        for word_tuple in perms:
            word = ''.join(word_tuple).lower()
            if word in DICTIONARY:
                possible.append(word)
        return possible

    def _get_permutations_draw(self, draw=[]):
        if not draw:
            draw = self.draw

        list_of_permutations = [
            permutations(draw, num_letters)
            for num_letters in range(1, NUM_LETTERS + 1)
        ]
        ret = [
            word_tuple for perm_group in list_of_permutations
            for word_tuple in perm_group
        ]
        return ret


def _is_valid_word(word, letters):
    """ checks to see if word is valid: can be made with letters
    if dictionary provided, check if word is in dictionary """
    # convert to lower case for testing
    word = word.lower()
    letters = [letter.lower() for letter in letters]

    # is word in the dictionary
    if word not in DICTIONARY:
        return False

    # check if we can remove all letters of the given word from letters
    try:
        letters_copy = letters.copy()
        for letter in word:
            letters_copy.remove(letter)
        # map(lambda letter: letters.remove(letter), word)
    except ValueError:
        return False
    return True
