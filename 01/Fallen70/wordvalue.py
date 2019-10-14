from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    return [
        word.strip()
        for word in open(DICTIONARY).readlines()
    ]

def calc_word_value( word ):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(
        LETTER_SCORES[letter.upper()]
        for letter in word
        if letter.isalpha()
    )

def max_word_value( words=None ):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = ( word for word in load_words() )
    return sorted((
        ( calc_word_value(word), word )
        for word in words
    ))[-1][1]

if __name__ == "__main__":
    pass # run unittests to validate
