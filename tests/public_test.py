import os
import time
import unittest
# import tempfile.NamedTemporaryFile as temp
from collections import defaultdict
from tempfile import NamedTemporaryFile as temp
from contextlib import contextmanager
from graph import Algorithms
from graph import Graph
from graph import GifMaker

LINUX = True
GIF_MAKER_TEST_PATH = ""

graph = None


@contextmanager
def tempOpen(path, mode):
    # if this fails there is nothing left to do anyways
    file = open(path, mode)

    try:
        yield file
    finally:
        file.close()
        os.remove(path)


#
def setUp():
    global graph, GIF_MAKER_TEST_PATH
    graph = Graph.Graph(0, dict())
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    print(timestamp)
    if LINUX:
        GIF_MAKER_TEST_PATH = 'tests/' + timestamp + '/'
        os.makedirs(GIF_MAKER_TEST_PATH, exist_ok=True)
    else:
        GIF_MAKER_TEST_PATH = timestamp + '/'
        os.makedirs(GIF_MAKER_TEST_PATH, exist_ok=True)


class TestAlgorithms(unittest.TestCase):
    def test_DFS_empty_input(self):
        msg = "DFS dont check empty input"

        graph.adjacency_list = None
        count = Algorithms.DFS(graph, 0)
        self.assertEqual(count, [], msg=msg)

    def test_DFS_path(self):
        # In algo you should run DFS using adj_list, from beginning to end
        msg = "DFS return different path from expected"
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = Algorithms.DFS(graph, 4)
        self.assertEqual([4, 0, 1, 3, 2, 5], path, msg=msg + "expected [4, 0, 1, 3, 2, 5]")

    def test_DFS_not_all_node_path(self):
        msg = "DFS return different path from expected"
        graph.adjacency_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        path = Algorithms.DFS(graph, 0)
        self.assertEqual(path, [0, 1, 3, 2], msg=msg + " expected [0, 1, 3, 2]")

    def test_BFS(self):
        msg = "BFS return different path from expected, path format [[node, layer]]"
        graph.adjacency_list = [[0, 1, 2], [3], [4], [0], [0]]
        path = Algorithms.BFS(graph, 0)
        self.assertEqual(path, [0, 1, 2, 3, 4], msg=msg)

    def test_BFS_empty_input(self):
        msg = "BFS dont check empty input"
        graph.adjacency_list = None
        output = Algorithms.BFS(graph, 0)
        self.assertEqual(output, [], msg=msg)


class TestGraph(unittest.TestCase):
    def test_graph_builder(self):
        msg = "Incorrect matrix for this nodes"
        local_graph = Graph.GraphBuilder.create_random_directed_graph()  # need new to check if he build ok
        self.assertEqual(local_graph.count_nodes, len(local_graph.adjacency_list), msg=msg)


class TestGifMaker(unittest.TestCase):

    def test_counter(self):
        # function returns not how many same_types but number of this elem
        msg = "GifMaker count_same_types count incorrect"
        path = GIF_MAKER_TEST_PATH
        with tempOpen(path + 'TYPE_1.txt', 'w'), tempOpen(path + 'TYPE_2.txt', 'w'):
            count = GifMaker.count_same_types(path, 'TYPE')
            self.assertEqual(count, 2 + 1, msg=msg)

    def test_name_creator(self):
        # creat temp files with special name to check how we calculate how many file of this type exist and how we
        # create new names
        msg = "GifMaker gif_name have problem with getting name of new gif"
        path = GIF_MAKER_TEST_PATH
        name_cases = ["TYPE_", "ONE_"]
        name = lambda count: name_cases[0] + str(count) + '.txt'  # to create same named files with diffent numbers
        with tempOpen(path + name(1), 'w'), tempOpen(path + name(2), 'w'), tempOpen(path + name(3), 'w'):
            file_name = GifMaker.gif_name(path, name(0))
            self.assertEqual(name_cases[0] + "4", file_name, msg=msg)

        name = lambda count: name_cases[1] + str(count) + '.txt'
        with tempOpen(path + name(1), 'w'), tempOpen(path + name(2), 'w'), tempOpen(path + name(3), 'w'), \
                tempOpen(path + name(4), 'w'):
            file_name = GifMaker.gif_name(path, name(0))
            self.assertEqual(name_cases[1] + "5", file_name, msg=msg)


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
        self.assertEqual({0: [], 1: [], 3: [1]}, graph.adjacency_list, msg)

    def test_add_non_exist_to_edge(self):
        msg = "Problem creating edge to non-exist node"
        graph = Graph.Graph(2, {0: [], 1: []})
        graph.add_edge(1, 3)
        self.assertEqual({0: [], 1: [3]}, graph.adjacency_list, msg)

    def test_all_non_exist(self):
        msg = "Problem creating edge from non-exist node to non-exist node"
        graph = Graph.Graph(2, {0: [], 1: []})
        graph.add_edge(2, 3)
        self.assertEqual({0: [], 1: [], 2: [3]}, graph.adjacency_list, msg)


class TestAlgorithmsGif(unittest.TestCase):
    def test_gif_BFS(self):
        msg = "wrong BFS working from gif"
        def_dict = defaultdict(list)
        test_list = [[0, 1, 2], [3], [4], [0], [0]]
        for i in range(len(test_list)):
            for elem in test_list[i]:
                def_dict[i].append(elem)

        test_adj_list = def_dict
        # print("dict", def_dict)
        local_graph = Graph.Graph(len(test_adj_list), dict())
        local_graph.adjacency_list = test_adj_list
        path = Algorithms.gif(local_graph, 0, Algorithms.BFS, GIF_MAKER_TEST_PATH)
        self.assertEqual(path, [0, 1, 2, 3, 4], msg=msg)

    def test_gif_DFS(self):
        msg = "wrong DFS working from gif"
        test_list = [[1, 2], [3, 1], [1], [2], [0, 5], [1, 4]]
        def_dict = defaultdict(list)
        for i in range(len(test_list)):
            for elem in test_list[i]:
                def_dict[i].append(elem)
        test_adj_list = def_dict
        local_graph = Graph.Graph(len(test_adj_list), dict())
        local_graph.adjacency_list = test_adj_list
        path = Algorithms.gif(local_graph, 0, Algorithms.DFS, GIF_MAKER_TEST_PATH)
        self.assertEqual(path, [0, 1, 3, 2], msg=msg)


setUp()
