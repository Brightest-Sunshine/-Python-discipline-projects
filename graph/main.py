import random

from graph import Algorithms, Graph

if __name__ == '__main__':

    graph = Graph.GraphBuilder.create_random_directed_graph()

    graph.draw_graph(graph)
    functions = [Algorithms.DFS, Algorithms.BFS]
    for fun in functions:
        random_node = random.randint(0, graph.count_nodes - 1)
        path = Algorithms.gif(graph, random_node, fun)