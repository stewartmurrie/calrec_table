import table

syms = ['Br', 'D', 'Ge', 'I']


def test_find_single_letter():
    letter = 'd'
    e = []
    assert table.findWord(letter, syms, e) is True
    assert e == ['D']


def test_find_double_letter():
    letters = 'ge'
    e = []
    assert table.findWord(letters, syms, e) is True
    assert e == ['Ge']


def test_negative_partial_match():
    letters = 'brick'
    e = []
    assert table.findWord(letters, syms, e) is False


def test_negative_find_single_letter():
    letters = 'f'
    e = []
    assert table.findWord(letters, syms, e) is False


def test_negative_find_double_letter():
    letters = 'fe'
    e = []
    assert table.findWord(letters, syms, e) is False


def test_find_word():
    letters = 'bridge'
    e = []
    assert table.findWord(letters, syms, e) is True
    assert e == ['Br', 'I', 'D', 'Ge']
