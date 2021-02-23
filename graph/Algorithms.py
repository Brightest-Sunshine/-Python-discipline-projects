import collections
from graph import Graph

NODE_COLOR = "red"
NODE_COLORS = ["red", "blue", "green", "orange", "grey", "pink"]
FORMAT = '.gv'
STYLE = "filled"
DFS_FOLDER = 'DFS_result\DFS_step_'
BFS_FOLDER = 'BFS_result\BFS_step_'


def DFS(graph: Graph, visited, node, counter=0, test_running=False):
    """
    :param graph: class object: The graph in which to run DFS
    :param visited: set: Numbers of visited nodes
    :param node: int: number of the current node
    :param counter: int: the chronological number of the node from the launch node
    :param test_running:bool : True if you running test. To prevent file creating
    :return: counter :return counter of the deepest visited node
    """
    if node not in visited:
        counter += 1
        if not test_running:
            file_name = DFS_FOLDER + str(counter) + FORMAT
            graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style=STYLE)
            graph.draw_graph(file_name=file_name, view=False, cleanup=True)
        visited.add(node)
        for neighbour in graph.adjacency_list[node]:
            counter = DFS(graph, visited, neighbour, counter, test_running)
    return counter


def BFS(graph: Graph, visited, node, test_running=False):
    """

    :param graph:  class object: The graph in which to run BFS
    :param visited: set: Numbers of visited nodes
    :param node: int: number of node from we run BFS
    :param test_running: bool : True if you running test. To prevent file creating
    :return: set of visited node if test_running False, else list[] path with [[visited_node, layer]]
    """
    path = []
    visited.add(node)
    if test_running:
        path = [[node, 0]]
    counter = 1
    color_count = 0
    if not test_running:
        file_name = BFS_FOLDER + str(counter) + FORMAT
        graph.graphviz_graph.node(str(node), fillcolor=NODE_COLORS[color_count], style=STYLE)
        graph.draw_graph(file_name=file_name, view=False, cleanup=True)
    color_count = 1
    queue = collections.deque([[node, color_count]])
    while queue:
        vertex, color_count = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                counter += 1
                file_name = BFS_FOLDER + str(counter) + FORMAT
                visited.add(neighbour)
                if not test_running:
                    graph.graphviz_graph.node(str(neighbour), fillcolor=NODE_COLORS[color_count], style=STYLE)
                    graph.draw_graph(file_name=file_name, view=False, cleanup=True)
                else:
                    path.append([neighbour, color_count + 1])
                queue.append([neighbour, color_count + 1])
    if test_running:
        return path
    return visited
