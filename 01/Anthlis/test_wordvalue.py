import pytest

from wordvalue import load_words, calc_word_value, max_word_value

words = load_words()


def test_load_words():
    assert len(words) == 235886
    assert words[0] == 'A'
    assert words[-1] == 'Zyzzogeton'
    assert ' ' not in ''.join(words)


def test_calc_word_value():
    assert calc_word_value('bob') == 7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56


def test_max_word_value():
    test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    assert max_word_value(test_words) == 'barbeque'
    assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'
    # cannot call with empty sequence
    with pytest.raises(ValueError):
        assert max_word_value(())


def test_non_scrabble_characters():
    # thanks Joakim
    assert max_word_value(["a", "åäö"]) == "a"