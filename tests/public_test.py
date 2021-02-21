import unittest
from graph import Algorithms
from graph import Graph


class TestG(unittest.TestCase):
    def test_DFS(self):
        graph = Graph.Graph()
        graph.adjacency_list = [[0, 1], [1, 2], [1], [0]]
        count = Algorithms.DFS(graph, set(), 0, test_running=1)
        self.assertEqual(count, 3)  # because we cant visit 4 from 0
        count = Algorithms.DFS(graph, set(), 3, test_running=1)
        self.assertEqual(count, 4)  # 3->0->1->2
        graph.adjacency_list = [[1], [2], [3], [0]]
        count = Algorithms.DFS(graph, set(), 0, test_running=1)
        self.assertEqual(count, 4)
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        count = Algorithms.DFS(graph, set(), 0, test_running=1)
        self.assertEqual(count, 4)  # cant visit 4 and 5 from 0
        count = Algorithms.DFS(graph, set(), 4, test_running=1)
        self.assertEqual(count, 6)  # can visit all

    def test_BFS(self):
        graph = Graph.Graph()
        graph.adjacency_list = [[0, 1], [1, 2], [1], [0]]
        path = Algorithms.BFS(graph, set(), 0, test_running=1)  # path format [[node, layer]]
        self.assertEqual(path, [[0, 0], [1, 2], [2, 3]])
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.BFS(graph, set(), 0, test_running=1)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]])
