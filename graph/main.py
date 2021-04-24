import random

from graph import Algorithms, Graph
from graph import GifMaker

if __name__ == '__main__':

    graph = Graph.GraphBuilder.create_random_directed_graph()

    graph.draw_graph(graph)
    functions = [Algorithms.DFS, Algorithms.BFS]
    save_paths = ['BFS_res', 'DFS_res']
    for fun in functions:
        random_node = random.choice(list(graph.adjacency_list.keys()))
        res_gif = Algorithms.gif(graph, random_node, fun)
        GifMaker.save(res_gif, save_paths.pop())

