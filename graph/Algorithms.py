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


def DFS_gif(graph: Graph, visited, node):  # Прослойка между самим алгоритмом для создания гифок
    created_files = []
    counter = DFS(graph, visited, node, created_files=created_files)
    GifMaker.make_gif_from_files(created_files)  # Создаем gif  из созданных файлов
    return counter


def BFS_gif(graph: Graph, visited, node):
    created_files = []
    visited = BFS(graph, visited, node, created_files=created_files)
    GifMaker.make_gif_from_files(created_files)  # Создаем gif  из созданных файлов
    return visited


def DFS(graph: Graph, visited, node, counter=0, test_running=False, created_files=None):
    """
    :param graph: class object: The graph in which to run DFS
    :param visited: set: Numbers of visited nodes
    :param node: int: number of the current node
    :param counter: int: the chronological number of the node from the launch node
    :param test_running:bool : True if you running test. To prevent file creating
    :param created_files: list[] of created files if we remembering them
    :return counter of the deepest visited node
    """
    if node not in visited:
        counter += 1
        if not test_running:
            file_name = DFS_FOLDER + str(counter) + FORMAT
            if created_files is not None:
                created_files.append(file_name + IMAGE_FORMAT)
            graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style=STYLE)  # Помечаем вершину
            graph.draw_graph(file_name=file_name, view=False, cleanup=True)  # Отрисовываем текущий шаг
        visited.add(node)
        for neighbour in graph.adjacency_list[node]:
            counter = DFS(graph, visited, neighbour, counter, test_running, created_files)
    return counter


def BFS(graph: Graph, visited, node, test_running=False, created_files=None):
    """

    :param graph:  class object: The graph in which to run BFS
    :param visited: set: Numbers of visited nodes
    :param node: int: number of node from we run BFS
    :param test_running: bool : True if you running test. To prevent file creating
    :param created_files: list[] of created files if we remembering them
    :return: set of visited node if test_running False, else list[] path with [[visited_node, layer]]
    """
    path = []
    visited.add(node)
    if test_running:
        path = [[node, 0]]
    counter = 1
    color_count = 0
    if not test_running:  # Чтобы не создавать файлы при прогоне теста
        file_name = BFS_FOLDER + str(counter) + FORMAT
        if created_files is not None:
            created_files.append(file_name + IMAGE_FORMAT)
        graph.graphviz_graph.node(str(node), fillcolor=NODE_COLORS[color_count], style=STYLE)  # Помечаем вершину цветом
        graph.draw_graph(file_name=file_name, view=False, cleanup=True)  # Отрисовываем ее
    color_count = 1
    queue = collections.deque([[node, color_count]])  # Кладем текущую вершину, и текущий цвет
    while queue:
        vertex, color_count = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                counter += 1
                file_name = BFS_FOLDER + str(counter) + FORMAT
                visited.add(neighbour)
                if created_files is not None:
                    created_files.append(file_name + IMAGE_FORMAT)
                if not test_running:  # Чтобы не создавать файлы при прогоне тестов + сохранять путь для проверки
                    graph.graphviz_graph.node(str(neighbour), fillcolor=NODE_COLORS[color_count], style=STYLE)
                    graph.draw_graph(file_name=file_name, view=False, cleanup=True)
                else:
                    path.append([neighbour, color_count + 1])  # Запоминаем, что мы тут были
                queue.append([neighbour, color_count + 1])  # Добавляем соседа, чтобы потом из него пройтись
    if test_running:
        return path

    return visited
