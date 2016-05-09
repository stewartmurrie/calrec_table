import sys


def findWord(word, symbols, elements):
    # Take a letter and a pair of letters from the front of the word;
    # ensure first letter is uppercase
    single = word[:1].title()
    double = word[:2].title()

    # nothing here, so unwind the stack
    if len(single) == 0:
        return True

    if single in symbols:
        elements.append(single)
        return findWord(word[1:], symbols, elements)
    else:
        return False


def table(filename):
    with open(filename) as f:
        symbols = [symbol.strip() for symbol in f]

    symbols.sort()
    print symbols

    word = "Zhinz"
    elements = []
    success = findWord(word, symbols, elements)
    print success
    print elements

if __name__ == "__main__":
    table(sys.argv[1])
