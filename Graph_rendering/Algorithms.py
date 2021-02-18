from Graph_rendering import Graph
import collections
import time

NODE_COLOR = "red"


def DFS(graph: Graph, visited, node, counter=0):  # done i guess
    if node not in visited:
        counter += 1
        file_name = 'DFS_step_' + str(counter) + '.gv'
        graph.graphviz_graph.node(str(node), fillcolor=NODE_COLOR, style="filled")
        graph.graphviz_graph.render(filename=file_name, view=True)
        visited.add(node)
        print(node)
        for neighbour in graph.adjacency_list[node]:
            counter = DFS(graph, visited, neighbour, counter)
    return counter


def BFS(graph: Graph, visited, node):
    queue = collections.deque([node])
    visited.add(node)
    graph.graph.node(str(node), fillcolor=NODE_COLOR)
    graph.draw_graph()
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                graph.graph.node(str(node), fillcolor=NODE_COLOR)
                graph.draw_graph()
                queue.append(neighbour)
    return
