import unittest
from assessment import (
    count_nested_keys,
    generate_collatz_sequence,
    validate_sudoku_board,
    find_anagrams,
    calculate_network_latency
)

class TestAssessment(unittest.TestCase):

    def test_count_nested_keys(self):
        self.assertEqual(count_nested_keys({}), 0)
        self.assertEqual(count_nested_keys({'a': 1}), 1)
        self.assertEqual(count_nested_keys({'a': {'b': {'c': {}}, 'd': {'e': {}}}}), 5)
        self.assertEqual(count_nested_keys({'a': {'b': 2}, 'c': [1, 2, 3]}), 2)
        self.assertEqual(count_nested_keys({'x': {}, 'y': {}, 'z': {}}), 3)
        self.assertEqual(count_nested_keys({'root': {'child1': {}, 'child2': {'grandchild': {}}}}), 4)

    def test_generate_collatz_sequence(self):
        self.assertEqual(generate_collatz_sequence(1), [1])
        self.assertEqual(generate_collatz_sequence(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(generate_collatz_sequence(11), [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(generate_collatz_sequence(0), [])
        self.assertEqual(generate_collatz_sequence(-5), [])
        self.assertEqual(len(generate_collatz_sequence(27)), 112)  # Just check length for long sequence

    def test_validate_sudoku_board(self):
        valid_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.assertTrue(validate_sudoku_board(valid_board))

        invalid_row = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 7]  # Duplicate in last row
        ]
        self.assertFalse(validate_sudoku_board(invalid_row))

        invalid_col = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        invalid_col[0][0] = 1  # Creates duplicate in first column
        self.assertFalse(validate_sudoku_board(invalid_col))

        invalid_box = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        invalid_box[0][0] = 9  # Creates duplicate in top-left box
        self.assertFalse(validate_sudoku_board(invalid_box))

        empty_board = [[0]*9 for _ in range(9)]
        self.assertTrue(validate_sudoku_board(empty_board))

        non_square_board = [[1, 2], [3, 4], [5, 6]]
        self.assertFalse(validate_sudoku_board(non_square_board))

    def test_find_anagrams(self):
        word_list = ['listen', 'silent', 'enlist', 'tinsel', 'hello', 'world', 'python']
        self.assertCountEqual(find_anagrams('listen', word_list), ['listen', 'silent', 'enlist', 'tinsel'])
        self.assertCountEqual(find_anagrams('python', word_list), ['python'])
        self.assertCountEqual(find_anagrams('program', word_list), [])

        self.assertCountEqual(find_anagrams('', ['', 'a', 'b']), [''])
        self.assertCountEqual(find_anagrams('a', ['a', 'aa', 'aaa']), ['a'])
        self.assertCountEqual(find_anagrams('abc', ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']), ['cba', 'bca', 'bac', 'cab', 'acb', 'abc'])

    def test_calculate_network_latency(self):
        routers = ['A', 'B', 'C', 'D']
        connections = [('A', 'B', 10), ('B', 'C', 20), ('C', 'D', 15)]
        self.assertEqual(calculate_network_latency(routers, connections), 20)

        routers2 = ['X', 'Y', 'Z']
        connections2 = [('X', 'Y', 5), ('Y', 'Z', 5)]
        self.assertEqual(calculate_network_latency(routers2, connections2), 5)

        routers3 = ['A', 'B', 'C']
        connections3 = [('A', 'B', 10), ('A', 'C', 20)]
        self.assertEqual(calculate_network_latency(routers3, connections3), 20)

        routers4 = ['A', 'B', 'C', 'D']
        connections4 = [('A', 'B', 10), ('C', 'D', 15)]
        self.assertEqual(calculate_network_latency(routers4, connections4), -1)

        routers5 = ['A']
        connections5 = []
        self.assertEqual(calculate_network_latency(routers5, connections5), -1)

        routers6 = ['A', 'B', 'C']
        connections6 = [('A', 'B', 10), ('B', 'C', 20), ('A', 'C', 5)]
        self.assertEqual(calculate_network_latency(routers6, connections6), 20)


if __name__ == '__main__':
    unittest.main(verbosity=2)