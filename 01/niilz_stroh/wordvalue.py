from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as f:
        words = f.read()
        f.close()
    return [word for word in words.split('\n')]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[char] for char in word.upper() if word in load_words()])

def max_word_value(wordList = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    wordCounts = [(calc_word_value(word), word) for word in wordList]
    return max(wordCounts)[1]

if __name__ == "__main__":
    print(load_words()[70:76])
    #abashedly, abashedness, abashless, abashlessly, abashment, abasia
    print(calc_word_value("hello")) # 8
    print(calc_word_value("abcdef")) # 0
    
    print(max_word_value(["hello", "day", "dolphin"]))
    # dolphin