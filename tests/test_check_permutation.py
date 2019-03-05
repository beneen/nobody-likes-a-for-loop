from unittest import TestCase

from string_manipulation.check_permutation import check_permutation


class TestCheck_permutation(TestCase):
    def test_check_permutation_empty(self):
        self.assertEqual(True, check_permutation("", ""))

    def test_check_permutation_empty_1(self):
        self.assertEqual(False, check_permutation("", "egg"))

    def test_check_permutation_empty_2(self):
        self.assertEqual(False, check_permutation("egg", ""))

    def test_check_permutation_is_permutation(self):
        self.assertEqual(True, check_permutation("egg", "gge"))

    def test_check_permutation_not_permutation(self):
        self.assertEqual(False, check_permutation("egg", "not"))

    def test_check_permutation_repeated_characters(self):
        self.assertEqual(False, check_permutation("egg", "eggg"))
