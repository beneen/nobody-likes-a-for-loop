from unittest import TestCase

from string_manipulation.check_one_away import check_one_away


class TestCheck_one_away(TestCase):
    def test_check_one_away_both_empty_is_not_one_away(self):
        self.assertEqual(True, check_one_away("", ""))

    def test_check_one_away_left_only_empty_is_one_away(self):
        self.assertEqual(False, check_one_away("", "egg"))

    def test_check_one_away_right_only_empty_is_one_away(self):
        self.assertEqual(False, check_one_away("egg", ""))

    def test_check_one_away_same_string_is_considered_one_away(self):
        self.assertEqual(True, check_one_away("egg", "egg"))

    def test_check_one_away_difference_of_greater_than_one_is_not_one_away(self):
        self.assertEqual(False, check_one_away("egge", "eg"))

    def test_check_one_away_completely_different_is_not_one_away(self):
        self.assertEqual(False, check_one_away("egg", "not"))

    def test_check_one_away_one_character_different_is_one_away(self):
        self.assertEqual(True, check_one_away("egg", "ege"))
