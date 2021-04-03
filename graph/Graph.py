import random
from dataclasses import dataclass

import numpy as np
from graphviz import Digraph

MIN_COUNT_NODES = 6
MAX_COUNT_NODES = 10
NO_WAY = 0
IS_WAY = 1
STYLE = "filled"
NODE_COLOR = "red"


@dataclass
class Graph:
    count_nodes: int
    adjacency_list: dict

    def add_edge(self, from_node, to_node):
        if from_node >= self.count_nodes:
            for i in range(self.count_nodes, from_node):
                self.adjacency_list[i] = []
            self.count_nodes = from_node + 1
            self.adjacency_list[from_node] = [to_node]
        else:
            self.adjacency_list[from_node].append(to_node)

        if to_node >= self.count_nodes:
            for i in range(self.count_nodes, to_node):
                self.adjacency_list[i] = []
            self.count_nodes = to_node + 1
            self.adjacency_list[to_node] = []
        return

    @staticmethod
    def draw_graph(graph, file_name='Graph.gv', view=False, cleanup=True, visited=None):
        if visited is None:
            visited = []
        graphviz = Digraph('G', filename=file_name, format='png')
        for node in range(graph.count_nodes):
            graphviz.node(str(node))
            if node in visited:
                graphviz.node(str(node), fillcolor=NODE_COLOR, style=STYLE)
            for neighbor in graph.adjacency_list[node]:
                graphviz.edge(str(node), str(neighbor))
        graphviz.render(filename=file_name, view=view, cleanup=cleanup)


class GraphBuilder:
    @staticmethod
    def create_random_directed_graph():
        count_nodes = random.randint(MIN_COUNT_NODES, MAX_COUNT_NODES)
        adj_matrix = np.random.randint(NO_WAY, IS_WAY + 1, size=(count_nodes, count_nodes))  # np.random [first, second)
        adj_list = GraphBuilder.create_adj_list_from_matrix(count_nodes, adj_matrix)

        return Graph(adjacency_list=adj_list, count_nodes=count_nodes)

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
    def init_graphviz(graph):
        graphviz = Digraph('G', filename='Graph.gv', format='png')
        for column in range(graph.count_nodes):
            for line in range(graph.count_nodes):
                if graph.adjacency_matrix[column][line] == IS_WAY:
                    graphviz.edge(str(column), str(line))
        return graphviz
