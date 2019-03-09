from unittest import TestCase

from dynamic_programming_algorithms.power_set import all_subsets


class TestAll_subsets(TestCase):
    def test_is_magic_index_zero(self):
        self.assertEqual([[], ['0']], all_subsets("0"))

    def test_is_magic_index_zero_one(self):
        self.assertEqual([[], ['0'], ['1'], ['0', '1']], all_subsets("01"))

    def test_is_magic_index_empty(self):
        self.assertEqual([[],], all_subsets(""))
