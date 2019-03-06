from unittest import TestCase

from string_manipulation.reverse_string import reverse_string


class TestReverse_string(TestCase):
    def test_reverse_string_space(self):
        self.assertEqual(" ", reverse_string(" "))

    def test_reverse_string_empty(self):
        self.assertEqual("", reverse_string(""))

    def test_reverse_string_same_character(self):
        self.assertEqual("aa", reverse_string("aa"))

    def test_reverse_string_palindrome(self):
        self.assertEqual("aba", reverse_string("aba"))

    def test_reverse_string_space_abcd(self):
        self.assertEqual("dcba", reverse_string("abcd"))
