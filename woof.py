#!/usr/bin/env python
"""
Replace all words with woofs, preserving punctuation.

Because Twitter loves Dogs.

Based on woof.py from @dariusk NaNoGenMo 2014.
https://github.com/dariusk/NaNoGenMo-2014/
"""

import re
import sys
import random
import argparse


def is_word(thing):
    found = re.match(r"\w+", thing, re.UNICODE)
    return found


def woof_woof(line, converter_fun):
    """Woofify a line"""
    woofed = []
    # Break line into words and non-words (e.g. punctuation and space)
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    for thing in things:
        if is_word(thing):
            woofed.append(converter_fun(thing))
        else:
            woofed.append(thing)
    return "".join(woofed)


def woof(word):
    """Woofify a word"""
    woofed = ""
    length = len(word)

    if length == 1:
        return capify("w", word)
    elif length == 2:
        return capify("wo", word)
    elif length == 3:
        return capify("woo", word)
    elif length == 4:
        return capify("woof", word)

    # Words longer than four will have:
    #  * first letter W
    #  * last letter F
    #  * middle with a random number of Es, then some Os

    # Number of EOs:
    eeohs = length - len("w") - len("f")
    # Number of Es:
    ees = random.randrange(1, eeohs)
    # Number of Os:
    ohs = eeohs - ees

    woofed = "w" + ("o" * ees) + ("o" * ohs) + "f"
    return capify(woofed, word)


def capify(word, reference):
    """Make sure word has the same capitalisation as reference"""
    new_word = ""

    # First check whole word before char-by-char
    if reference.islower():
        return word.lower()
    elif reference.isupper():
        return word.upper()

    # Char-by-char checks
    for i, c in enumerate(reference):
        if c.isupper():
            new_word += word[i].upper()
        else:
            new_word += word[i]
    return new_word


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Replace all words with woofs, preserving punctuation.")
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, help="Input text")
    parser.add_argument('-t', '--translation', action="store_true",
                        help="Output a line-by-line translation")
    args = parser.parse_args()

#     for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
    for line in args.infile:
        #line = line.decode("utf-8-sig").rstrip()  # No BOM
        if args.translation:
            print()
            #print(line.encode("utf-8"))
        #print(woof_woof(line, woof).encode("utf-8"))
        print(woof_woof(line, woof))

# End of file
