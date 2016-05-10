import table

syms = ['B', 'Br', 'D', 'Ge', 'I', ' ', 'R', 'E', 'De']


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
    assert len(e) is 0


def test_negative_find_single_letter():
    letters = 'f'
    e = []
    assert table.findWord(letters, syms, e) is False
    assert len(e) is 0

def test_negative_find_double_letter():
    letters = 'fe'
    e = []
    assert table.findWord(letters, syms, e) is False
    assert len(e) is 0

def test_find_word():
    letters = 'bridge'
    e = []
    assert table.findWord(letters, syms, e) is True
    assert e == ['Br', 'I', 'D', 'Ge']


def test_find_word_2():
    letters = 'bid'
    e = []
    assert table.findWord(letters, syms, e) is True
    assert e == ['B', 'I', 'D']


def test_find_word_2():
    letters = 'bride'
    e = []
    assert table.findWord(letters, syms, e) is True
    assert e == ['Br', 'I', 'De']


def test_find_phrase():
    letters = 'bid bridge'
    e = []
    assert table.findWord(letters, syms, e) is True
    assert e == ['B', 'I', 'D', ' ', 'Br', 'I', 'D', 'Ge']
