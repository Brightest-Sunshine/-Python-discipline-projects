import random
from collections import defaultdict
from dataclasses import dataclass
import argparse
import numpy as np
from graphviz import Digraph
from graph import GifMaker

MIN_COUNT_NODES = 6
MAX_COUNT_NODES = 10
NO_WAY = 0
IS_WAY = 1
STYLE = "filled"
NODE_COLOR = "red"
LINUX = True


@dataclass
class Graph:
    adjacency_list: defaultdict(list)

    def add_edge(self, from_node, to_node):
        this = self.adjacency_list.get(from_node, [])
        this.append(to_node)
        self.adjacency_list[from_node] = this
        to = self.adjacency_list.get(to_node, [])
        if not to:
            self.adjacency_list[to_node] = to

    @staticmethod
    def draw_graph(graph, file_name='Graph', view=False, cleanup=True, visited=None):
        if visited is None:
            visited = []
        graphviz = Digraph('G', filename=file_name, format='png')
        for node in graph.adjacency_list.keys():
            graphviz.node(str(node))
            if node in visited:
                graphviz.node(str(node), fillcolor=NODE_COLOR, style=STYLE)
            for neighbor in graph.adjacency_list.get(node, []):
                graphviz.edge(str(node), str(neighbor))
        return graphviz.render(filename=file_name, view=view, cleanup=cleanup)


class GraphBuilder:
    @staticmethod
    def create_random_directed_graph():
        count_nodes = random.randint(MIN_COUNT_NODES, MAX_COUNT_NODES)
        adj_matrix = np.random.randint(NO_WAY, IS_WAY + 1, size=(count_nodes, count_nodes))  # np.random [first, second)
        adj_list = GraphBuilder.create_adj_list_from_matrix(count_nodes, adj_matrix)

        return Graph(adjacency_list=adj_list)

    @staticmethod
    def create_adj_list_from_matrix(nodes, matrix):
        adjacency_list = {}
        for column in range(nodes):
            adj_nodes = []
            for line in range(nodes):
                if matrix[column][line] == IS_WAY:
                    adj_nodes.append(line)
            adjacency_list[column] = adj_nodes
        return adjacency_list

    @staticmethod
    def create_from_file(path):  # Expected format "1 0"
        graph = Graph({})
        with open(path, 'r') as file:
            for line in file:
                from_node, to_node = line.split()
                graph.add_edge(int(from_node), int(to_node))

        return graph


class RunFromCLI:
    # default_method =  located in set and run because if here, import Errors occurs.
    if LINUX:
        default_input = "tests/default_graph.txt"
    else:
        default_input = "default_graph.txt"
    default_output = "result"

    @staticmethod
    def run_from_file(args):
        graph = RunFromCLI.set_and_run_input(args.input_path)
        start = RunFromCLI.find_start_node(args.starting_node, graph)
        res_gif = RunFromCLI.set_and_run_method(graph, args.method, start, args.draw)
        RunFromCLI.set_and_run_output(args.output_path, res_gif)

    @staticmethod
    def find_start_node(start_node, graph):
        if start_node is None:
            start_node = list(graph.adjacency_list.keys())[0]
        else:
            start_node = int(start_node)
        return start_node

    @staticmethod
    def set_and_run_method(graph, method, start_node_ind, draw):
        from graph import Algorithms
        default_method = Algorithms.DFS
        if method:
            if method == "dfs":
                res_gif = Algorithms.gif(graph, start_node_ind, Algorithms.DFS, draw=draw)
            elif method == "bfs":
                res_gif = Algorithms.gif(graph, start_node_ind, Algorithms.BFS, draw=draw)
            else:
                print("Unknown method, run ", str(default_method), "as default")
                res_gif = Algorithms.gif(graph, start_node_ind, default_method, draw=draw)
        else:
            print("No method chosen, run ", str(default_method), "as default")
            res_gif = Algorithms.gif(graph, start_node_ind, default_method, draw=draw)
        return res_gif

    @staticmethod
    def set_and_run_input(input):

        if input:
            graph = GraphBuilder.create_from_file(input)
        else:
            graph = GraphBuilder.create_from_file(RunFromCLI.default_input)
        return graph

    @staticmethod
    def set_and_run_output(output, res_gif):
        if output:
            GifMaker.save(res_gif, output)
        else:
            GifMaker.save(res_gif, RunFromCLI.default_output)


if __name__ == '__main__':  #
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', dest='input_path', help='path to file with graph'
                                                                '(default=' + str(RunFromCLI.default_input) + ")")
    parser.add_argument('--method', dest='method', help='choose method to run(bfs/dfs)(default = DFS)')
    parser.add_argument('--output_file', dest='output_path', help='path to saving gif'
                                                                  '(default = ' + str(RunFromCLI.default_output) + ")")
    parser.add_argument('--start', dest='starting_node', help='start method from certain node'
                                                              '(default=first from node in input file)')
    parser.add_argument('--draw', action='store_true', help='making png file of method steps',
                        default=False)
    args = parser.parse_args()
    print(args)
    RunFromCLI.run_from_file(args)
