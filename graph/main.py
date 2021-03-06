import random

from graph import Algorithms, Graph

if __name__ == '__main__':
    graph = Graph.Graph()

    graph.draw_graph()
    random_node = random.randint(0, graph.count_nodes - 1)  #
    visited = set()
    Algorithms.DFS_gif(graph, visited, random_node)
    graph.draw_graph()
    visited = set()
    #Algorithms.BFS_gif(graph, visited, random_node)  # TODO Убрать что основной граф меняется в процессе прогона
