"""
-----
Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards.

**Incomplete**
-----
"""
import unittest

class TestPermutation(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty(self):
        self.assertEqual(is_palindrome(""), True)




def split_string(text):
    firstpart = text[0:len(text) // 2]
    secondpart = text[len(text) // 2 if len(text) % 2 == 0 else ((len(text) // 2) + 1):]
    return firstpart, secondpart

def is_palindrome(text):
    firstpart, secondpart = split_string(text)
    return set(firstpart) == set(secondpart)

if __name__ == "__main__":
    text = input("insert text:")
    print(is_palindrome(text))
    unittest.main()
