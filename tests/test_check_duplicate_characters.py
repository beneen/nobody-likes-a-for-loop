from unittest import TestCase

from string_manipulation.duplicate_characters import check_duplicate_characters


class TestCheck_duplicate_characters(TestCase):
    def test_check_duplicate_characters_empty(self):
        self.assertEqual("", check_duplicate_characters(""))

    def test_check_duplicate_characters_space(self):
        self.assertEqual("", check_duplicate_characters(" "))

    def test_check_duplicate_characters_single_character(self):
        self.assertEqual("", check_duplicate_characters("e"))

    def test_check_duplicate_characters_two_characters_same(self):
        self.assertEqual("e", check_duplicate_characters("ee"))

    def test_check_duplicate_characters_two_characters_same_with_duplicate_spaces(self):
        self.assertEqual("e ", check_duplicate_characters("ee  "))

