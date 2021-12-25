import unittest
from .caves import parse, build_graph, is_special


class TestCavesFunctions(unittest.TestCase):
    def setUp(self):
        self.raw_map = '/home/gyogy/code/advent/inputs/test'
        self.nodes = parse(self.raw_map)

    def test_parse_func(self):
        expected = [
            'start', 'A',
            'start', 'b',
            'A', 'c',
            'A', 'b',
            'b', 'd',
            'A', 'end',
            'b', 'end']
        result = parse(self.raw_map)
        self.assertEqual(expected, result)

    def test_build_graph(self):
        expected = {
            'start': ['A', 'b'],
            'A': ['start', 'c', 'b', 'end'],
            'b': ['start', 'A', 'd', 'end'],
            'c': ['A'],
            'd': ['b'],
            'end': ['A', 'b']
        }
        result = build_graph(self.nodes)
        self.assertEqual(expected, result)

    def test_is_special(self):
        special = 'c'

        result = is_special('c', special)
        self.assertTrue(result)
        self.assertEqual(is_special.count, 1)

        result = is_special('c', special)
        self.assertTrue(result)
        self.assertEqual(is_special.count, 2)

        result = is_special('c', special)
        self.assertFalse(result)
        self.assertEqual(is_special.count, 2)
