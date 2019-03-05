from unittest import TestCase

from string_manipulation.escape_spaces import escape_spaces


class TestReplace_spaces(TestCase):
    def test_replace_spaces_empty(self):
        self.assertEqual("", escape_spaces("", ""))

    def test_replace_spaces_empty_1(self):
        self.assertEqual("%20", escape_spaces(" ", ""))
