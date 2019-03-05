from unittest import TestCase

from string_manipulation.unique import unique


class TestUnique(TestCase):
    def test_unique_empty(self):
        self.assertEqual(True, unique(""))

    def test_unique_empty_1(self):
        self.assertEqual(True, unique("a"))

    def test_unique_empty_2(self):
        self.assertEqual(True, unique("a "))

