from unittest import TestCase

from string_manipulation.rotate_matrix import rotate_matrix


class TestRotate_matrix(TestCase):
    def test_rotate_matrix_empty(self):
        self.assertEqual("", rotate_matrix(""))
