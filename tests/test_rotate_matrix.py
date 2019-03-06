from unittest import TestCase

from string_manipulation.rotate_matrix import rotate_matrix


class TestRotate_matrix(TestCase):
    def test_rotate_matrix_example(self):
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_rotate_matrix_empty(self):
        self.assertEqual([], rotate_matrix([[]]))

    def test_rotate_matrix_one_by_one(self):
        self.assertEqual([[1]], rotate_matrix([[1]]))
