from unittest import TestCase

from dynamic_programming_algorithms.magic_index import magic_index


class TestMagic_index(TestCase):
    def test_is_magic_index_zero(self):
        self.assertEqual((True,), magic_index("0"))

    def test_is_magic_index_empty(self):
        self.assertEqual((), magic_index(""))

    def test_is_magic_index_one(self):
        self.assertEqual((False,), magic_index("1"))

    def test_is_magic_index_one_one(self):
        self.assertEqual((False, True), magic_index("11"))

    def test_is_magic_index_0123(self):
        self.assertEqual((True, True, True, True), magic_index("0123"))

    def test_is_magic_index_end_aligning(self):
        self.assertEqual((False, False, False, False, False, True), magic_index("123455"))

    def test_is_magic_index_none_aligning(self):
        self.assertEqual((False, False, False, False, False, False), magic_index("123456"))

    def test_is_magic_index_none_all_same(self):
        self.assertEqual((False, False, False, False, False, False), magic_index("888888"))
