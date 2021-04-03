import collections
from graph import Graph
from graph import GifMaker

NODE_COLOR = "red"
NODE_COLORS = ["red", "blue", "green", "orange", "grey", "pink"]
FORMAT = '.gv'
IMAGE_FORMAT = '.png'
STYLE = "filled"
DFS_FOLDER = 'DFS_result\DFS_step_'
BFS_FOLDER = 'BFS_result\BFS_step_'


def gif(graph: Graph, node: int, method, visited: list = None, test: bool = False):
    created_files = []
    if test:
        path = method(graph, node, visited=visited, created_files=created_files)
    else:
        path = method(graph, node, visited=visited, created_files=created_files, draw=graph.draw_graph)
    if not test:
        GifMaker.make_gif_from_files(created_files)  # Creating GIFs from created files
    return path


def DFS(graph: Graph, node: int, visited: list = None, created_files: list = None,
        draw=lambda graph, visited, file_name: None):
    """
    :param graph: class object: The graph in which to run DFS
    :param visited: list: Numbers of visited nodes, basically path
    :param node: int: number of the current node
    :param created_files: list[] of created files if we remembering them(example for gif)
    :param draw:function get graph,visited,file name
    :return visited: list: Numbers of visited nodes, basically path
    """
    if visited is None:  # write this way because of mutable default
        visited = []
    if created_files is None:
        created_files = []
    if graph is None or graph.adjacency_list is None:
        return 1
    if node not in visited:
        visited.append(node)
        counter = len(visited)
        file_name = DFS_FOLDER + str(counter) + FORMAT
        draw(graph, visited=visited, file_name=file_name)
        if created_files is not None:
            created_files.append(file_name + IMAGE_FORMAT)
        for neighbour in graph.adjacency_list[node]:
            visited = DFS(graph, neighbour, created_files=created_files, visited=visited, draw=draw)
    return visited


def BFS(graph: Graph, node: int, visited=None, created_files: list = None, draw=lambda graph, visited, file_name: None):
    """

    :param draw: function get graph,visited,file name
    :param graph:  class object: The graph in which to run BFS
    :param visited: set: Numbers of visited nodes
    :param node: int: number of node from we run BFS
    :param created_files: list[] of created files if we remembering them
    :return: list[] path with [[visited_node, layer]]
    """
    if visited is None:  # write this way because of mutable default
        visited = []
    if created_files is None:
        created_files = []
    if graph is None or graph.adjacency_list is None:
        return 1
    visited.append(node)
    path = [[node, 0]]
    counter = 1
    file_name = BFS_FOLDER + str(counter) + FORMAT
    created_files.append(file_name + IMAGE_FORMAT)
    draw(graph, visited=visited, file_name=file_name)
    layer_count = 1
    queue = collections.deque([[node, layer_count]])  # We put the current vertex, and the current color
    while queue:
        vertex, layer_count = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                counter += 1
                file_name = BFS_FOLDER + str(counter) + FORMAT
                visited.append(neighbour)
                created_files.append(file_name + IMAGE_FORMAT)
                draw(graph, visited=visited, file_name=file_name)
                path.append([neighbour, layer_count + 1])  # Remember that we were here
                queue.append([neighbour, layer_count + 1])  # Adding a neighbor to then walk out of it
    return path
