"""
-----
Implement an algorithm to determine id a string has all unique characters.
-----
"""

import unittest

class TestUnique(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty(self):
        self.assertEqual(unique(""), True)

    def test_empty_1(self):
        self.assertEqual(unique("a"), True)

    def test_empty_2(self):
        self.assertEqual(unique("a "), True)



def unique(s):
    print(s)
    return len(set(s)) == len(s)

if __name__ == "__main__":
    text = input("insert text:")
    print(unique(text))
    unittest.main()



