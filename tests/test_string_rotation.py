from unittest import TestCase

from string_manipulation.string_rotation import string_rotation


class TestString_rotation(TestCase):
    def test_string_rotation_example_given(self):
        self.assertEqual(True , string_rotation("waterbottle", "erbottlewat"))

    def test_string_rotation_example_given_modified(self):
        self.assertEqual(False , string_rotation("waterbottle", "rebottlewat"))

    def test_string_rotation_empty(self):
        self.assertEqual(True , string_rotation("", ""))

    def test_string_rotation_one_character(self):
        self.assertEqual(True , string_rotation("a", "a"))