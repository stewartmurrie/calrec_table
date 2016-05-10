import sys
import pdb

def findWord(word, symbols, elements):
    #print word, elements
    #pdb.set_trace()

    if len(word) == 0:
        return True

    # Take a letter and a pair of letters from the front of the word;
    # ensure first letter is uppercase
    single = word[:1].title()
    double = word[:2].title()
    result = False
    # nothing here, so unwind the stack
    if len(single) == 1 and single in symbols:
        elements.append(single)
        result = findWord(word[1:], symbols, elements)
        if result is True:
            return True
        else:
            del elements[-1]
    if len(double) == 2 and double in symbols:
        elements.append(double)
        return findWord(word[2:], symbols, elements)

    return False


def table(filename):
    with open(filename) as f:
        symbols = [symbol.rstrip('\n') for symbol in f]

    symbols.sort()
    print symbols

    word = "axes sharp"
    elements = []
    success = findWord(word, symbols, elements)
    print success
    print elements

if __name__ == "__main__":
    table(sys.argv[1])
