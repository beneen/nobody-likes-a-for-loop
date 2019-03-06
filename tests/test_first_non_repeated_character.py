from unittest import TestCase

from string_manipulation.first_non_repeated_character import first_non_repeated_character


class TestFirst_non_repeated_character(TestCase):
    def test_first_non_repeated_character_space(self):
        self.assertEqual(" ", first_non_repeated_character(" "))

    def test_first_non_repeated_characte_one_character(self):
        self.assertEqual("a", first_non_repeated_character("a"))

    def test_first_non_repeated_characte_first_non_repeated(self):
        self.assertEqual(" ", first_non_repeated_character("aabb "))

    def test_first_non_repeated_characte_empty(self):
        self.assertEqual("a", first_non_repeated_character("abcd"))

