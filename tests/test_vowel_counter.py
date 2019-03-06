from unittest import TestCase

from string_manipulation.vowel_count import vowel_counter


class TestVowel_counter(TestCase):
    def test_vowel_counter_empty(self):
        self.assertEqual(0, vowel_counter(""))

    def test_vowel_counter_one_vowel(self):
        self.assertEqual(1, vowel_counter("a"))

    def test_vowel_counter_one_consonant(self):
        self.assertEqual(0, vowel_counter("x"))

    def test_vowel_counter_two_vowels(self):
        self.assertEqual(2, vowel_counter("aa"))

    def test_vowel_counter_two_consonants(self):
        self.assertEqual(0, vowel_counter("xx"))
