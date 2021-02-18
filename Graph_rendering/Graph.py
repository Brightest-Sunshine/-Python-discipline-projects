import random
import numpy as np
from graphviz import Digraph

MIN_COUNT_NODES = 4
MAX_COUNT_NODES = 6
NO_WAY = 0
IS_WAY = 1


class Graph:
    def __init__(self):
        self.count_nodes = random.randint(MIN_COUNT_NODES, MAX_COUNT_NODES)
        self.adjacency_matrix = np.random.randint(NO_WAY, IS_WAY + 1, size=(self.count_nodes, self.count_nodes))
        self.adjacency_list = self.create_adjacency_list()
        self.graphviz_graph = self.init_graphviz()

    def create_adjacency_list(self):
        adjacency_list = {}
        for column in range(self.count_nodes):
            nodes = []
            for line in range(self.count_nodes):
                if self.adjacency_matrix[column][line] == IS_WAY:
                    nodes.append(line)
            adjacency_list[column] = nodes
        return adjacency_list

    def init_graphviz(self):
        graph = Digraph('G', filename='Graph.gv')
        for column in range(self.count_nodes):
            for line in range(self.count_nodes):
                if self.adjacency_matrix[column][line] == IS_WAY:
                    graph.edge(str(column), str(line))
        return graph

    def draw_graph(self):
        self.graphviz_graph.render(filename='Graph.gv', view=True)
        return
