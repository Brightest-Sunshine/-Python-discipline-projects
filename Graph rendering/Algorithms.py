import Graph
import collections

NODE_COLOR = "blue"


def DFS(graph: Graph, visited, node):
    if node not in visited:
        graph.graph.node(str(node), fillcolor=NODE_COLOR)
        graph.draw_graph()
        visited.add(node)
        for neighbour in graph.adjacency_list[node]:
            DFS(graph, visited, neighbour)
    return


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
