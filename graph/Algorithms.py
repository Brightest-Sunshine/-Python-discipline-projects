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


def DFS_gif(graph: Graph, visited, node):  # The layer between the algorithm itself for creating GIFs
    created_files = []
    counter = DFS(graph, visited, node, created_files=created_files)
    GifMaker.make_gif_from_files(created_files)  # Creating GIFs from created files
    return counter


def BFS_gif(graph: Graph, visited, node):
    created_files = []
    visited = BFS(graph, visited, node, created_files=created_files)
    GifMaker.make_gif_from_files(created_files)  # Creating GIFs from created files
    return visited


def DFS(graph: Graph, visited, node, counter=0, no_images =False, created_files=None):
    """
    :param graph: class object: The graph in which to run DFS
    :param visited: list: Numbers of visited nodes, basically path
    :param node: int: number of the current node
    :param counter: int: the chronological number of the node from the launch node
    :param no_images:bool : True if you dont need img. To prevent file creating
    :param created_files: list[] of created files if we remembering them(example for gif)
    :return counter of the deepest visited node
    """
    if node not in visited:
        counter += 1
        if not no_images:
            file_name = DFS_FOLDER + str(counter) + FORMAT
            if created_files is not None:
                created_files.append(file_name + IMAGE_FORMAT)
            graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style=STYLE)  # mark node
            graph.draw_graph(file_name=file_name, view=False, cleanup=True)  # Drawing the current step
        visited.append(node)
        for neighbour in graph.adjacency_list[node]:
            counter = DFS(graph, visited, neighbour, counter, no_images, created_files)
    return counter


def BFS(graph: Graph, visited, node, no_images=False, created_files=None):
    """

    :param graph:  class object: The graph in which to run BFS
    :param visited: set: Numbers of visited nodes
    :param node: int: number of node from we run BFS
    :param no_images: bool : True if you dont need img. To prevent file creating
    :param created_files: list[] of created files if we remembering them
    :return: list[] path with [[visited_node, layer]]
    """
    path = []
    visited.add(node)
    if no_images:
        path = [[node, 0]]
    counter = 1
    color_count = 0
    if not no_images:  # To avoid creating files when running the test
        file_name = BFS_FOLDER + str(counter) + FORMAT
        if created_files is not None:
            created_files.append(file_name + IMAGE_FORMAT)
        graph.graphviz_graph.node(str(node), fillcolor=NODE_COLORS[color_count], style=STYLE)  # mark node with color
        graph.draw_graph(file_name=file_name, view=False, cleanup=True)  # draw this step
    color_count = 1
    queue = collections.deque([[node, color_count]])  # We put the current vertex, and the current color
    while queue:
        vertex, color_count = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                counter += 1
                file_name = BFS_FOLDER + str(counter) + FORMAT
                visited.add(neighbour)
                if created_files is not None:
                    created_files.append(file_name + IMAGE_FORMAT)
                if not no_images:  # To avoid creating files when running tests + save the path for verification
                    graph.graphviz_graph.node(str(neighbour), fillcolor=NODE_COLORS[color_count], style=STYLE)
                    graph.draw_graph(file_name=file_name, view=False, cleanup=True)
                else:
                    path.append([neighbour, color_count + 1])  # Remember that we were here
                queue.append([neighbour, color_count + 1])  # Adding a neighbor to then walk out of it
    return path
