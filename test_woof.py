#!/usr/bin/env python
"""
Unit tests for woof.py
"""

import unittest
import woof
import re


class TestIt(unittest.TestCase):

    def sanity_check(self, word, out):
        self.assertEqual(len(word), len(out))

        # Check pattern
        if len(word) > 4:
            found = re.match("w[o]+[o]+f", out, re.IGNORECASE)
            self.assertTrue(found)

        # Check caps
        for i in range(len(word)):
            self.assertEqual(word[i].isupper(),
                             out[i].isupper())

    def test_1_letter_word(self):
        word = "I"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "W")

    def test_2_letter_word(self):
        word = "on"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "wo")

    def test_3_letter_word(self):
        word = "The"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Woo")

    def test_4_letter_word(self):
        word = "book"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "woof")

    def test_capify_1(self):
        word = "woof"
        reference = "Book"
        out = woof.capify(word, reference)
        self.assertEqual(out, "Woof")

    def test_capify_2(self):
        word = "woof"
        reference = "BOOK"
        out = woof.capify(word, reference)
        self.assertEqual(out, "WOOF")

    def test_capify_3(self):
        word = "woof"
        reference = "book"
        out = woof.capify(word, reference)
        self.assertEqual(out, "woof")

    def test_capify_4(self):
        word = "woof"
        reference = "BoOk"
        out = woof.capify(word, reference)
        self.assertEqual(out, "WoOf")

    def test_upper_4_letter_word(self):
        word = "BOOK"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "WOOF")

    def test_capped_4_letter_word(self):
        word = "Book"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Woof")

    def test_mixcapped_4_letter_word(self):
        word = "BooK"
        out = woof.woof(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "WooF")

    def test_5_letter_word(self):
        word = "clock"
        out = woof.woof(word)
        self.sanity_check(word, out)

    def test_6_letter_word(self):
        word = "whales"
        out = woof.woof(word)
        self.sanity_check(word, out)

    def test_13_letter_word(self):
        word = "Extraordinary"
        out = woof.woof(word)
        self.sanity_check(word, out)

    def test_line(self):
        line = "On the bus"
        out = woof.woof_woof(line, woof.woof)
        self.assertEqual(out, "Wo woo woo")

    def test_is_word_1(self):
        thing = "word"
        out = woof.is_word(thing)
        self.assertTrue(out)

    def test_is_word_2(self):
        thing = ";"
        out = woof.is_word(thing)
        self.assertFalse(out)

    def test_line_punctuation(self):
        line = "On the bus? On the bus."
        out = woof.woof_woof(line, woof.woof)
        self.assertEqual(out, "Wo woo woo? Wo woo woo.")


if __name__ == '__main__':
    unittest.main()

# End of file
