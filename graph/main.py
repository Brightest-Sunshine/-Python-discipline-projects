import random

from graph import Algorithms, Graph

if __name__ == '__main__':
    graph = Graph.Graph()

    graph.draw_graph()
    random_node = random.randint(0, graph.count_nodes - 1)  #
    path = list()
    copy_graph = graph.copy()  # So as not to change the colors in the main graph!
    Algorithms.DFS_gif(copy_graph, path, random_node)

    copy_graph = graph.copy()
    visited = set()
    path = Algorithms.BFS_gif(copy_graph, visited, random_node)
