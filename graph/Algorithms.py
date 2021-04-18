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
LINUX = True
if LINUX:
    PATH = 'gifs/'
    TEST_PATH = 'tests/'
else:
    PATH = 'gifs\\'
    TEST_PATH = None


def gif(graph: Graph, node: int, method, result_path: str = PATH):
    created_files = []
    path = method(graph, node, created_files=created_files, draw=graph.draw_graph)
    GifMaker.make_gif_from_files(created_files, result_path)
    return path


def DFS(graph: Graph, node: int, created_files: list = None, draw=lambda graph, visited, file_name: None):
    return __DFS(graph, node, created_files=created_files, draw=draw)


def __DFS(graph: Graph, node: int, visited: list = None, created_files: list = None,
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
        return []
    if node not in visited:
        visited.append(node)
        counter = len(visited)
        file_name = DFS_FOLDER + str(counter) + FORMAT
        draw(graph, visited=visited, file_name=file_name)
        if created_files is not None:
            created_files.append(file_name + IMAGE_FORMAT)
        for neighbour in graph.adjacency_list[node]:
            visited = __DFS(graph, neighbour, created_files=created_files, visited=visited, draw=draw)
    return visited


def BFS(graph: Graph, node: int, created_files: list = None, draw=lambda graph, visited, file_name: None):
    """

    :param draw: function get graph,visited,file name
    :param graph:  class object: The graph in which to run BFS
    :param node: int: number of node from we run BFS
    :param created_files: list[] of created files if we remembering them
    :return: list[] path with [[visited_node, layer]]
    """

    if created_files is None:
        created_files = []
    if graph is None or graph.adjacency_list is None:
        return []
    visited = [node]
    file_name = lambda count: BFS_FOLDER + str(count) + FORMAT

    path = [node]
    counter = 1
    created_files.append(file_name(counter) + IMAGE_FORMAT)
    draw(graph, visited=visited, file_name=file_name(counter))
    queue = collections.deque([node])  # We put the current vertex, and the current color
    while queue:
        vertex = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                counter += 1
                visited.append(neighbour)
                created_files.append(file_name(counter) + IMAGE_FORMAT)
                draw(graph, visited=visited, file_name=file_name(counter))
                path.append(neighbour)  # Remember that we were here
                queue.append(neighbour)  # Adding a neighbor to then walk out of it
    return path
