from unittest import TestCase

from string_manipulation.first_non_repeated_character import first_non_repeated_character


class TestFirst_non_repeated_character(TestCase):
    def test_check_anagram_space(self):
        self.assertEqual(" ", first_non_repeated_character(" "))

    def test_check_anagram_one_character(self):
        self.assertEqual("a", first_non_repeated_character("a"))

    def test_check_anagram_space_first_non_repeated(self):
        self.assertEqual(" ", first_non_repeated_character("aabb "))

    def test_check_anagram_empty(self):
        self.assertEqual("a", first_non_repeated_character("abcd"))

