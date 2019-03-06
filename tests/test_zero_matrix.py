from unittest import TestCase

from string_manipulation.zero_matrix import zero_matrix


class TestZero_matrix(TestCase):
    def test_zero_matrix_zero_in_every_row(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], zero_matrix([[0, 2, 3], [4, 5, 0], [7, 0, 9]]))

    def test_zero_matrix_no_zeros(self):
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], zero_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_zero_matrix_all_zeros(self):
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], zero_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_zero_matrix_zero(self):
        self.assertEqual([[0]], zero_matrix([[0]]))

    def test_zero_matrix_all_empty(self):
        self.assertEqual([], zero_matrix([]))