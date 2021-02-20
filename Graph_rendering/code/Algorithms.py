import collections
from task import Graph

NODE_COLOR = "red"
NODE_COLORS = ["red", "blue", "green", "orange", "grey", "pink"]


def DFS(graph: Graph, visited, node, counter=0, test_running=0):
    if node not in visited:
        counter += 1
        if test_running == 0:
            file_name = 'DFS_result\DFS_step_' + str(counter) + '.gv'
            graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style="filled")
            graph.draw_graph(file_name=file_name, view=False, cleanup=True)
        visited.add(node)
        for neighbour in graph.adjacency_list[node]:
            counter = DFS(graph, visited, neighbour, counter, test_running)
    return counter


def BFS(graph: Graph, visited, node, test_running=0):
    path = []
    visited.add(node)
    if test_running:
        path = [[node, 0]]
    counter = 1
    color_count = 0
    if test_running == 0:
        file_name = 'BFS_result\BFS_step_' + str(counter) + '.gv'
        graph.graphviz_graph.node(str(node), fillcolor=NODE_COLORS[color_count], style="filled")
        graph.draw_graph(file_name=file_name, view=False, cleanup=True)
    color_count = 1
    queue = collections.deque([[node, color_count]])
    while queue:
        vertex, color_count = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                counter += 1
                file_name = 'BFS_result\BFS_step_' + str(counter) + '.gv'
                visited.add(neighbour)
                if test_running == 0:
                    graph.graphviz_graph.node(str(neighbour), fillcolor=NODE_COLORS[color_count], style="filled")
                    graph.draw_graph(file_name=file_name, view=False, cleanup=True)
                else:
                    path.append([neighbour, color_count + 1])
                queue.append([neighbour, color_count + 1])
    if test_running:
        return path
    return visited
