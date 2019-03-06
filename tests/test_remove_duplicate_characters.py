from unittest import TestCase

from string_manipulation.remove_duplicate_chatacters import remove_duplicate_characters


class TestRemove_duplicate_characters(TestCase):
    def test_reverse_words_empty(self):
        self.assertEqual("", remove_duplicate_characters(""))

    def test_reverse_words_single_character(self):
        self.assertEqual("a", remove_duplicate_characters("a"))

    def test_reverse_words_double_characters_same(self):
        self.assertEqual("", remove_duplicate_characters("aa"))

    def test_reverse_words_example(self):
        self.assertEqual("abc", remove_duplicate_characters("abc"))
