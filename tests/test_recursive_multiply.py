from unittest import TestCase

from dynamic_programming_algorithms.recursive_multiply import recursive_multiply


class TestRecursive_multiply(TestCase):


    class TestMultiply(TestCase):
        def test_recursive_multiply_zero(self):
            self.assertEqual(0, recursive_multiply("0", "0"))

        def test_recursive_multiply_zero_one(self):
            self.assertEqual(0, recursive_multiply("0", "1"))

        def test_recursive_multiply_one_zero(self):
            self.assertEqual(0, recursive_multiply("1", "0"))

        def test_recursive_multiply_one_one(self):
            self.assertEqual(1, recursive_multiply("1", "1"))

        def test_recursive_multiply_one_one(self):
            self.assertEqual(1, recursive_multiply("1", "1"))
