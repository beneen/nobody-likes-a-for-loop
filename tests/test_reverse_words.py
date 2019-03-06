from unittest import TestCase

from string_manipulation.reverse_words import reverse_words


class TestReverse_words(TestCase):
    def test_reverse_words_empty(self):
        self.assertEqual("", reverse_words(""))

    def test_reverse_words_space(self):
        self.assertEqual(" ", reverse_words(" "))

    def test_reverse_words_single_character(self):
        self.assertEqual("a", reverse_words("a"))

    def test_reverse_words_example(self):
        self.assertEqual("b and a", reverse_words("a and b"))