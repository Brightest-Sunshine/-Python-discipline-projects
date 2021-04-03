import os
import unittest
from contextlib import contextmanager
from graph import Algorithms
from graph import Graph
from graph import GifMaker

LINUX = True
if LINUX:
    GIF_MAKER_TEST_PATH = 'tests/'
else:
    GIF_MAKER_TEST_PATH = ''


@contextmanager
def tempOpen(path, mode):
    # if this fails there is nothing left to do anyways
    file = open(path, mode)

    try:
        yield file
    finally:
        file.close()
        os.remove(path)


class TestAlgorithms(unittest.TestCase):
    def test_DFS_empty_input(self):
        msg = "DFS dont check empty input"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = None
        count = Algorithms.DFS(graph, 0)
        self.assertEqual(count, 1, msg=msg)

    def test_DFS_path(self):
        # In algo you should run DFS using adj_list, from beginning to end
        msg = "DFS return different path from expected"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = Algorithms.DFS(graph, 4)
        self.assertEqual([4, 0, 1, 3, 2, 5], path, msg=msg + "expected [4, 0, 1, 3, 2, 5]")

    def test_DFS_not_all_node_path(self):
        msg = "DFS return different path from expected"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = Algorithms.DFS(graph, 0)
        self.assertEqual(path, [0, 1, 3, 2], msg=msg + " expected [0, 1, 3, 2]")

    def test_BFS(self):
        msg = "BFS return different path from expected, path format [[node, layer]]"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.BFS(graph, 0)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]], msg=msg)

    def test_BFS_empty_input(self):
        msg = "BFS dont check empty input"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = None
        output = Algorithms.BFS(graph, 0)
        self.assertEqual(output, 1, msg=msg)


class TestGraph(unittest.TestCase):
    def test_graph_builder(self):
        msg = "Incorrect matrix for this nodes"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        self.assertEqual(graph.count_nodes, len(graph.adjacency_list), msg=msg)


class TestGifMaker(unittest.TestCase):

    def test_counter(self):
        # function returns not how many same_types but number of this elem
        msg = "GifMaker count_same_types count incorrect"
        path = GIF_MAKER_TEST_PATH
        with tempOpen(path + 'TYPE_1.txt', 'w'), tempOpen(path + 'TYPE_2.txt', 'w'):
            count = GifMaker.count_same_types('TYPE', test=True)
            self.assertEqual(count, 2 + 1, msg=msg)

    def test_name_creator(self):
        msg = "GifMaker gif_name have problem with getting name of new gif"
        path = GIF_MAKER_TEST_PATH
        with tempOpen(path + 'TYPE_1.txt', 'w'), tempOpen(path + 'TYPE_2.txt', 'w'), tempOpen(path + 'TYPE_3.txt', 'w'):
            file_name = GifMaker.gif_name("TYPE_1.txt", test=True)
            self.assertEqual("TYPE_4", file_name, msg=msg)

        with tempOpen(path + 'ONE_1.txt', 'w'), tempOpen(path + 'ONE_2.txt', 'w'), tempOpen(path + 'ONE_3.txt', 'w'), \
                tempOpen(path + 'ONE_4.txt', 'w'):
            file_name = GifMaker.gif_name("ONE_1.txt", test=True)
            self.assertEqual("ONE_5", file_name, msg=msg)


class TestAddEdge(unittest.TestCase):
    def test_add_edge_of_exist_node(self):
        msg = "Problem creating edge of exist node"
        graph = Graph.Graph(2, {0: [], 1: []})
        graph.add_edge(0, 1)
        self.assertEqual({0: [1], 1: []}, graph.adjacency_list, msg)

    def test_add_non_exist_from_edge(self):
        msg = "Problem creating edge from non-exist node"
        graph = Graph.Graph(2, {0: [], 1: []})
        graph.add_edge(3, 1)
        self.assertEqual({0: [], 1: [], 2: [], 3: [1]}, graph.adjacency_list, msg)

    def test_add_non_exist_to_edge(self):
        msg = "Problem creating edge to non-exist node"
        graph = Graph.Graph(2, {0: [], 1: []})
        graph.add_edge(1, 3)
        self.assertEqual({0: [], 1: [3], 2: [], 3: []}, graph.adjacency_list, msg)

    def test_all_non_exist(self):
        msg = "Problem creating edge from non-exist node to non-exist node"
        graph = Graph.Graph(2, {0: [], 1: []})
        graph.add_edge(2, 3)
        self.assertEqual({0: [], 1: [], 2: [3], 3: []}, graph.adjacency_list, msg)


class TestAlgorithmsGif(unittest.TestCase):
    def test_gif_BFS(self):
        msg = "wrong BFS working from gif"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.gif(graph, 0, Algorithms.BFS, test=True)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]], msg=msg)

    def test_gif_DFS(self):
        msg = "wrong DFS working from gif"
        graph = Graph.GraphBuilder.create_random_directed_graph()
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = Algorithms.gif(graph, 0, Algorithms.DFS, test=True)
        self.assertEqual(path, [0, 1, 3, 2], msg=msg)
