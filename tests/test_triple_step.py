from unittest import TestCase

from dynamic_programming_algorithms.triple_step import triple_step


class TestTriple_step(TestCase):
    def test_triple_step_zero(self):
        self.assertEqual(1, triple_step(0))

    def test_triple_step_one(self):
        self.assertEqual(1, triple_step(1))

    def test_triple_step_two(self):
        self.assertEqual(2, triple_step(2))

    def test_triple_step_three(self):
        self.assertEqual(4, triple_step(3))

    def test_triple_step_four(self):
        self.assertEqual(7, triple_step(4))
