import os
import time
import unittest
from collections import defaultdict, namedtuple
from contextlib import contextmanager
from graph import Algorithms
from graph import Graph
from graph import GifMaker

LINUX = False
TEST_PATH = ""
TEST_EXAMPLES = ""
graph = None


def setUp():
    global graph, TEST_PATH
    graph = Graph.Graph(dict())
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    print(timestamp)
    if LINUX:
        TEST_PATH = 'tests/' + timestamp + '/'
        os.makedirs(TEST_PATH, exist_ok=True)
    else:
        TEST_PATH = timestamp + '/'
        os.makedirs(TEST_PATH, exist_ok=True)


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


class TestGifMaker(unittest.TestCase):
    def test_create_from_graph(self):
        pass


class TestRunFromCLI(unittest.TestCase):
    def setUp(self):
        self.CLI_default_graph = Graph.RunFromCLI.set_and_run_input(None)
        self.CLI_default_input = Graph.RunFromCLI.default_input
        self.CLI_default_output = Graph.RunFromCLI.default_output
        self.CLI_default_draw = False
        self.msg_start_node = "Wrong CLI starting node results"
        self.msg_input = "Wrong CLI input results"
        self.msg_output = "Wrong CLI output results"
        self.msg_method = "Wrong CLI method results"
        self.msg_all = "Wrong CLI run from files results"

    def test_find_start_node_not_None(self):
        start_node = "1"
        res = Graph.RunFromCLI.find_start_node(start_node, graph)
        self.assertEqual(res, int(start_node), msg=self.msg_start_node)

    def test_find_start_node_None(self):
        start_node = None
        this_graph = Graph.Graph({2: [], 1: []})
        res = Graph.RunFromCLI.find_start_node(start_node, this_graph)
        self.assertEqual(res, list(this_graph.adjacency_list.keys())[0], msg=self.msg_start_node)

    def test_set_and_run_input_not_None(self):
        this_input = TEST_EXAMPLES + "special_example.txt"
        this_graph = Graph.RunFromCLI.set_and_run_input(this_input)
        self.assertEqual(this_graph.adjacency_list, {1: [2, 0], 2: [3], 3: [0], 0: [5], 5: [1]}, msg=self.msg_input)

    def test_set_and_run_input_None(self):
        this_graph = Graph.RunFromCLI.set_and_run_input(None)
        self.assertEqual(this_graph.adjacency_list, {0: [5], 1: [2, 0], 2: [3], 3: [0], 5: [1]}, msg=self.msg_input)

    def test_set_and_run_method_not_None(self):
        this_method = Algorithms.DFS
        start = 0
        res = Graph.RunFromCLI.set_and_run_method(self.CLI_default_graph, this_method, start, self.CLI_default_draw)
        self.assertEqual(str(type(res[0])), "<class 'imageio.core.util.Array'>", msg=self.msg_method)

    def test_set_and_run_method_None(self):
        this_method = None
        start = 0
        res = Graph.RunFromCLI.set_and_run_method(self.CLI_default_graph, this_method, start, self.CLI_default_draw)
        self.assertEqual(str(type(res[0])), "<class 'imageio.core.util.Array'>", msg=self.msg_method)

    def test_set_and_run_output_None(self):
        this_method = None
        this_output = None
        start = 0
        res_gif = Graph.RunFromCLI.set_and_run_method(self.CLI_default_graph, this_method, start, self.CLI_default_draw)
        Graph.RunFromCLI.set_and_run_output(this_output, res_gif)
        if TEST_EXAMPLES == '':
            self.assertTrue(Graph.RunFromCLI.default_output + ".gif" in os.listdir(), msg=self.msg_output)
        else:
            self.assertTrue(Graph.RunFromCLI.default_output + ".gif" in os.listdir(TEST_EXAMPLES), msg=self.msg_output)

    def test_set_and_run_output_not_None(self):

        file_name = "output_result"
        this_output = TEST_PATH + file_name
        this_method = None
        start = 0
        res_gif = Graph.RunFromCLI.set_and_run_method(self.CLI_default_graph, this_method, start, self.CLI_default_draw)
        Graph.RunFromCLI.set_and_run_output(this_output, res_gif)
        self.assertTrue(file_name + ".gif" in os.listdir(TEST_PATH), msg=self.msg_output)

    def test_run_from_file(self):
        this_input = self.CLI_default_input
        file_name = "full_run_result"
        this_output = TEST_PATH + file_name
        this_method = None
        draw = self.CLI_default_draw
        start = 0
        args = namedtuple('named_field_for_test', ['draw', 'output_path', 'input_path', 'method', 'starting_node'])
        this_args = args(draw, this_output, this_input, this_method, start)
        Graph.RunFromCLI.run_from_file(this_args)
        self.assertTrue(file_name + ".gif" in os.listdir(TEST_PATH), msg=self.msg_all)


class TestGraphBuilder(unittest.TestCase):
    def test_create_from_file(self):
        msg = "Wrong creating file from graph"

        example_file = TEST_EXAMPLES + "default_graph.txt"
        res = Graph.GraphBuilder.create_from_file(example_file)
        self.assertEqual(res.adjacency_list, {1: [2, 0], 2: [3], 3: [0], 0: [5], 5: [1]}, msg=msg)


class TestAddEdge(unittest.TestCase):
    def test_add_edge_of_exist_node(self):
        msg = "Problem creating edge of exist node"
        graph = Graph.Graph({0: [], 1: []})
        graph.add_edge(0, 1)
        self.assertEqual({0: [1], 1: []}, graph.adjacency_list, msg)

    def test_add_non_exist_from_edge(self):
        msg = "Problem creating edge from non-exist node"
        graph = Graph.Graph({0: [], 1: []})
        graph.add_edge(3, 1)
        self.assertEqual({0: [], 1: [], 3: [1]}, graph.adjacency_list, msg)

    def test_add_non_exist_to_edge(self):
        msg = "Problem creating edge to non-exist node"
        graph = Graph.Graph({0: [], 1: []})
        graph.add_edge(1, 3)
        self.assertEqual({0: [], 1: [3], 3: []}, graph.adjacency_list, msg)

    def test_all_non_exist(self):
        msg = "Problem creating edge from non-exist node to non-exist node"
        graph = Graph.Graph({0: [], 1: []})
        graph.add_edge(2, 3)
        self.assertEqual({0: [], 1: [], 2: [3], 3: []}, graph.adjacency_list, msg)


class TestAlgorithmsGif(unittest.TestCase):
    def test_gif_BFS(self):
        msg = "wrong BFS working from gif"
        local_graph = Graph.GraphBuilder.create_random_directed_graph()
        gifs_res = Algorithms.gif(local_graph, 0, Algorithms.BFS)
        self.assertEqual(str(type(gifs_res[0])), "<class 'imageio.core.util.Array'>", msg=msg)

    def test_gif_DFS(self):
        msg = "wrong DFS working from gif"
        local_graph = Graph.GraphBuilder.create_random_directed_graph()
        gif_res = Algorithms.gif(local_graph, 0, Algorithms.DFS)
        self.assertEqual(str(type(gif_res[0])), "<class 'imageio.core.util.Array'>", msg=msg)


setUp()

