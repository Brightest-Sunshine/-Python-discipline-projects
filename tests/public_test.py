import unittest
from graph import Algorithms
from graph import Graph
from graph import GifMaker


class TestAlgorithms(unittest.TestCase):
    def test_DFS(self):
        graph = Graph.Graph()
        graph.adjacency_list = [[0, 1], [1, 2], [1], [0]]
        count = Algorithms.DFS(graph, list(), 0, no_images=True)
        self.assertEqual(len(count), 3)  # because we cant visit 4 from 0
        count = Algorithms.DFS(graph, list(), 3, no_images=True)
        self.assertEqual(len(count), 4)  # 3->0->1->2
        graph.adjacency_list = [[1], [2], [3], [0]]
        count = Algorithms.DFS(graph, list(), 0, no_images=True)
        self.assertEqual(len(count), 4)
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        count = Algorithms.DFS(graph, list(), 0, no_images=True)
        self.assertEqual(len(count), 4)  # cant visit 4 and 5 from 0
        count = Algorithms.DFS(graph, list(), 4, no_images=True)
        self.assertEqual(len(count), 6)  # can visit all

        # new test because now we return path
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = []
        count = Algorithms.DFS(graph, path, 0, no_images=True)
        self.assertEqual(path, [0, 1, 3, 2])
        path = []
        count = Algorithms.DFS(graph, path, 4, no_images=True)
        self.assertEqual([4, 0, 1, 3, 2, 5], path)

    def test_BFS(self):
        graph = Graph.Graph()
        graph.adjacency_list = [[0, 1], [1, 2], [1], [0]]
        path = Algorithms.BFS(graph, list(), 0, no_images=True)  # path format [[node, layer]]
        self.assertEqual(path, [[0, 0], [1, 2], [2, 3]])
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.BFS(graph, list(), 0, no_images=True)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]])

    def test_gif(self):
        graph = Graph.Graph()
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = list()
        path = Algorithms.gif(graph, path, 0, Algorithms.DFS, no_images=True, test=True)
        self.assertEqual(path, [0, 1, 3, 2])
        path = list()
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.gif(graph, path, 0, Algorithms.BFS, no_images=True, test=True)
        self.assertEqual(path, [[0, 0], [1, 2], [2, 2], [3, 3], [4, 3]])


class TestGraph(unittest.TestCase):
    def test_graph_builder(self):
        graph = Graph.Graph()
        nodes, matrix = Graph.GraphBuilder.create_random_directed_graph()
        self.assertEqual(nodes, len(matrix))
        graph.count_nodes = nodes
        graph.adjacency_matrix = matrix
        adj_list = Graph.GraphBuilder.create_adj_list_from_matrix(graph)
        self.assertEqual(len(adj_list), len(matrix))
        path = []
        for i in range(len(matrix[0])):
            if matrix[0][i]:
                path.append(i)
        self.assertEqual(path, adj_list[0])

    def test_graph(self):
        graph = Graph.Graph()
        graph_copy = graph.copy()
        self.assertEqual(graph_copy.count_nodes, graph.count_nodes)
        self.assertEqual(graph_copy.adjacency_list, graph.adjacency_list)
        self.assertNotEqual(graph_copy.graphviz_graph, graph.graphviz_graph)


class TestGifMaker(unittest.TestCase):
    def test_counter(self):
        # function returns not how many same_types but number of this elem
        counter = GifMaker.count_same_types('TYPE', test=True)
        self.assertEqual(counter, 3 + 1)
        counter = GifMaker.count_same_types('ONE', test=True)
        self.assertEqual(counter, 4 + 1)

    def test_name_creator(self):
        file_name = GifMaker.gif_name("TYPE_1.txt", test=True)
        self.assertEqual("TYPE_4", file_name)
        file_name = GifMaker.gif_name("ONE_1.txt", test=True)
        self.assertEqual("ONE_5", file_name)
