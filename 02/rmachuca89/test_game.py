import re
import game

NUM_LETTERS = 7
TEST_WORDS = ("bob", "julian", "pybites", "quit", "barbeque")
FIXED_DRAW = list("garytev".upper())


def test_calc_word_value():
    expected = (7, 13, 14, 13, 21)
    for word, value in zip(TEST_WORDS, expected):
        my_value = game.calc_word_value(word)
        assert my_value == value


def test_max_word_value():
    expected = "barbeque"
    expected_default = "benzalphenylhydrazone"
    assert game.max_word_value(TEST_WORDS) == expected
    assert game.max_word_value() == expected_default


def test_gen_draw():
    letter_str = "".join(game.gen_draw())
    # Duplicate braces (`{{}}`) to escape them
    DRAW_PATTERN = fr"^[A-Z]{{{NUM_LETTERS}}}$"
    DRAW_RE = re.compile(DRAW_PATTERN)
    assert DRAW_RE.match(letter_str)


def test_is_letters_in_draw():
    word = "GARYTEV"
    assert game.is_letters_in_draw(word, FIXED_DRAW)
    word = "ARE"
    assert game.is_letters_in_draw(word, FIXED_DRAW)
    word = "F"
    assert not game.is_letters_in_draw(word, FIXED_DRAW)
    word = "GARETTA"
    assert not game.is_letters_in_draw(word, FIXED_DRAW)


def test_is_word_in_dict():
    word = "GARYTEV"
    assert not game.is_word_in_dict(word)
    word = "ARE"
    assert game.is_word_in_dict(word)


def test_calc_optimal_word():
    assert game.calc_optimal_word(FIXED_DRAW) == ("garvey", 13)


def test_calc_user_score():
    values = (7, 13, 14, 13, 6)
    optimal = (24, 22, 17, 22, 12)
    expected = (
        0.2916666666666667,
        0.5909090909090909,
        0.8235294117647058,
        0.5909090909090909,
        0.5,
    )
    for index, (value, opt) in enumerate(zip(values, optimal)):
        assert expected[index] == game.calc_user_score(value, opt)
