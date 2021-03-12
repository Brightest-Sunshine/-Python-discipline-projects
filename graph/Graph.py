import random
import numpy as np
from graphviz import Digraph

MIN_COUNT_NODES = 6  # 6 10
MAX_COUNT_NODES = 10
NO_WAY = 0
IS_WAY = 1


class Graph:
    def __init__(self):
        self.count_nodes, self.adjacency_matrix = GraphBuilder.create_random_directed_graph()
        self.adjacency_list = GraphBuilder.create_adj_list_from_matrix(self)
        self.graphviz_graph = GraphBuilder.init_graphviz(self)

    def copy(self):  # make copy with different graphviz
        copy_graph = Graph()
        copy_graph.count_nodes = self.count_nodes
        copy_graph.adjacency_matrix = self.adjacency_matrix
        copy_graph.adjacency_list = self.adjacency_list
        copy_graph.graphviz_graph = GraphBuilder.init_graphviz(copy_graph)
        return copy_graph

    def draw_graph(self, file_name='Graph.gv', view=True, cleanup=False):
        self.graphviz_graph.render(filename=file_name, view=view, cleanup=cleanup)
        return


class GraphBuilder:
    @staticmethod
    def create_random_directed_graph():
        count_nodes = random.randint(MIN_COUNT_NODES, MAX_COUNT_NODES)
        adj_matrix = np.random.randint(NO_WAY, IS_WAY + 1, size=(count_nodes, count_nodes))  # np.random [first, second)
        return count_nodes, adj_matrix

    @staticmethod
    def create_adj_list_from_matrix(graph):
        adjacency_list = {}
        for column in range(graph.count_nodes):
            nodes = []
            for line in range(graph.count_nodes):
                if graph.adjacency_matrix[column][line] == IS_WAY:
                    nodes.append(line)
            adjacency_list[column] = nodes
        return adjacency_list

    @staticmethod
    def init_graphviz(graph):
        graphviz = Digraph('G', filename='Graph.gv', format='png')
        for column in range(graph.count_nodes):
            for line in range(graph.count_nodes):
                if graph.adjacency_matrix[column][line] == IS_WAY:
                    graphviz.edge(str(column), str(line))
        return graphviz
