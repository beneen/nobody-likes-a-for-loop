from unittest import TestCase

from string_manipulation.string_compression import string_compression


class TestString_compression(TestCase):

    def test_string_compression_example_given(self):
        self.assertEqual("a2b1c5a3", string_compression("aabcccccaaa"))

    def test_string_compression_empty(self):
        self.assertEqual("", string_compression(""))

    def test_string_compression_compressed_string_not_smaller(self):
        self.assertEqual("ab", string_compression("ab"))

    def test_string_compression_compressed_single_character(self):
        self.assertEqual("k", string_compression("k"))

    def test_string_compression_space(self):
        self.assertEqual(" ", string_compression(" "))


