from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY, "r") as word_list:
        words = word_list.read().strip().split("\n")
    return words

def calc_word_value(word):
    val = 0
    for l in word:
        if l.isalpha():
            val += LETTER_SCORES[l.upper()]
    return val

def max_word_value(words = load_words()):
    max_val = 0
    max_word = ''

    for word in words:
        val = calc_word_value(word)
        if val > max_val:
            max_val = val
            max_word = word

    return max_word

if __name__ == "__main__":
    pass
