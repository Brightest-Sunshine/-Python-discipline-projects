import os
import unittest
from contextlib import contextmanager
from graph import Algorithms
from graph import Graph
from graph import GifMaker

LINUX = True
if LINUX:
    GIF_MAKER_TEST_PATH = 'GifMaker_folder/'
else:
    GIF_MAKER_TEST_PATH = 'GifMaker_folder\\'


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
    # def test_DFS_count_visited_node(self):
    #     msg = "DFS not visited some nodes"
    #     graph = Graph.Graph()
    #     graph.adjacency_list = [[0, 1], [1, 2], [1], [0]]
    #     count = Algorithms.DFS(graph, list(), 0, no_images=True)
    #     self.assertEqual(len(count), 3, msg=msg + "expected 3, because we cant visit 4 from 0 in [[0, 1], [1, 2], "
    #                                               "[1], [0]]")
    #     count = Algorithms.DFS(graph, list(), 3, no_images=True)
    #     self.assertEqual(len(count), 4, msg=msg + " expected 4, 3->0->1->2 in [[0, 1], [1, 2], [1], [0]] ") # 3->0->1->2
    #     graph.adjacency_list = [[1], [2], [3], [0]]
    #     count = Algorithms.DFS(graph, list(), 0, no_images=True)
    #     self.assertEqual(len(count), 4, msg=msg + " expected 4")
    #     graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
    #     count = Algorithms.DFS(graph, list(), 0, no_images=True)
    #     self.assertEqual(len(count), 4, msg=msg + "expected 4, cant visit 4 and 5 from 0 in  [[1, 2], [3, 1], [1], "
    #                                               "[2], [0, 5], [1, 4]]")  # cant visit 4 and 5 from 0
    #     count = Algorithms.DFS(graph, list(), 4, no_images=True)
    #     self.assertEqual(len(count), 6, msg=msg + " expected 6")  # can visit all

    def test_DFS_empty_input(self):
        msg = "DFS dont check empty input"
        graph = Graph.Graph()
        graph.adjacency_list = None
        count = Algorithms.DFS(graph, 0, no_images=True)
        self.assertEqual(count, 1, msg=msg)

    def test_DFS_path(self):
        # In algo you should run DFS using adj_list, from beginning to end
        msg = "DFS return different path from expected"
        graph = Graph.Graph()
        # new test because now we return path
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = []
        path = Algorithms.DFS(graph, 0, no_images=True)
        self.assertEqual(path, [0, 1, 3, 2], msg=msg + " expected [0, 1, 3, 2]")
        path = Algorithms.DFS(graph, 4, no_images=True)
        self.assertEqual([4, 0, 1, 3, 2, 5], path, msg=msg + "expected [4, 0, 1, 3, 2, 5]")

    def test_BFS(self):
        msg = "BFS return different path from expected, path format [[node, layer]]"
        graph = Graph.Graph()
        graph.adjacency_list = [[0, 1], [1, 2], [1], [0]]
        path = Algorithms.BFS(graph, 0, no_images=True)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 3]], msg=msg)
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.BFS(graph, 0, no_images=True)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]], msg=msg)

    def test_BFS_empty_input(self):
        msg = "BFS dont check empty input"
        graph = Graph.Graph()
        graph.adjacency_list = None
        output = Algorithms.BFS(graph, 0, no_images=True)
        self.assertEqual(output, 1, msg=msg)

    def test_gif(self):
        msg = "wrong algorithms working from gif"
        graph = Graph.Graph()
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = list()
        path = Algorithms.gif(graph, path, 0, Algorithms.DFS, no_images=True, test=True)
        self.assertEqual(path, [0, 1, 3, 2], msg=msg)
        path = list()
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.gif(graph, path, 0, Algorithms.BFS, no_images=True, test=True)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]], msg=msg)


class TestGraph(unittest.TestCase):
    def test_graph_builder(self):
        msg = "Incorrect matrix for this nodes"
        graph = Graph.Graph()
        nodes, matrix = Graph.GraphBuilder.create_random_directed_graph()
        self.assertEqual(nodes, len(matrix), msg=msg)
        graph.count_nodes = nodes
        graph.adjacency_matrix = matrix
        adj_list = Graph.GraphBuilder.create_adj_list_from_matrix(graph)
        msg = "incorrect adjacency list from matrix"
        self.assertEqual(len(adj_list), len(matrix), msg=msg)
        path = []
        for i in range(len(matrix[0])):
            if matrix[0][i]:
                path.append(i)
        self.assertEqual(path, adj_list[0], msg=msg)

    def test_graph(self):
        graph = Graph.Graph()
        graph_copy = graph.copy()
        msg = "Incorrect graph data copying"
        self.assertEqual(graph_copy.count_nodes, graph.count_nodes, msg=msg)
        self.assertEqual(graph_copy.adjacency_list, graph.adjacency_list, msg=msg)
        msg = "Dont create new graphviz for copy"
        self.assertNotEqual(graph_copy.graphviz_graph, graph.graphviz_graph, msg=msg)


class TestGifMaker(unittest.TestCase):

    def test_counter(self):
        # function returns not how many same_types but number of this elem
        msg = "GifMaker count_same_types count incorrect"
        path = GIF_MAKER_TEST_PATH
        with tempOpen(path + 'TYPE_1.txt', 'w'), tempOpen(path + 'TYPE_2.txt'
                , 'w'):
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
