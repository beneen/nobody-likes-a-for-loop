from unittest import TestCase

from string_manipulation.anagram_checker import check_anagram


class TestCheck_anagram(TestCase):
    def test_check_anagram_empty(self):
        self.assertEqual(True, check_anagram("", ""))

    def test_check_anagram_one_empty_one_space(self):
        self.assertEqual(False, check_anagram(" ", ""))

    def test_check_anagram_empty_one_empty(self):
        self.assertEqual(False, check_anagram("a", ""))