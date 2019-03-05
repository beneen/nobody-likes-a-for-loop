from unittest import TestCase

from string_manipulation.palindrome_permutation import is_palindrome_permutation


class TestIs_palindrome(TestCase):
    def test_is_palindrome_empty(self):
        self.assertEqual(True, is_palindrome_permutation(""))
