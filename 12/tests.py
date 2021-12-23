import unittest
from .caves import parse, build_graph


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
