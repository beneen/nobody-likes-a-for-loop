from unittest import TestCase

from string_manipulation.find_duplicate_characters import find_duplicate_characters


class TestFind_duplicate_characters(TestCase):
    def test_find_duplicate_characters_empty(self):
        self.assertEqual(set(), find_duplicate_characters(""))
    def test_find_duplicate_characters_one_character(self):
        self.assertEqual(set(), find_duplicate_characters("a"))
    def test_find_duplicate_characters_two_characters(self):
        self.assertEqual({('a', 2)} , find_duplicate_characters("aa"))