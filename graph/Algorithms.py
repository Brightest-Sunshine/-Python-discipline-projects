"""
Algorithms.py
====================================
Module containing all graph algo i use in my Graph-rendering project
"""

import collections
from typing import Optional

from graph.Graph import Graph
from graph import GifMaker


def gif(graph: Graph, node: int, method, draw=False) -> list:
    """

    :param graph: graph:  class object: The graph in which to run method
    :param node: int: index of starting node
    :param method: function: method what used for visualisation
    :param draw: bool: Make step files during gif creation
    :return: list(imageio.class): result of imageio working with graph steps during method run

    """
    path = method(graph, node)
    gif_img = GifMaker.build_from_graph(graph, path, draw)
    return gif_img


def DFS(graph: Graph, node: int) -> list:
    """
    :param graph:  class object: The graph in which to run DFS
    :param node: int: index of starting node
    :return: visited: list: index of visited nodes, basically path

    """
    return __DFS(graph, node)


def __DFS(graph: Graph, node: int, visited: Optional[list] = None) -> list:
    """
    :param graph: class object: The graph in which to run DFS
    :param visited: list: Numbers of visited nodes, basically path
    :param node: int: number of the current node
    :return visited: list: Numbers of visited nodes, basically path
    """
    if visited is None:  # write this way because of mutable default
        visited = []
    if graph is None or graph.adjacency_list is None:
        return []
    if node not in visited:
        visited.append(node)
        for neighbour in graph.adjacency_list[node]:
            visited = __DFS(graph, neighbour, visited=visited)
    return visited


def BFS(graph: Graph, node: int) -> list:
    """
    :param graph:  class object: The graph in which to run BFS
    :param node: int: number of node from we run BFS
    :return: list[] path

    """

    if graph is None or graph.adjacency_list is None:
        return []
    visited = [node]
    path = [node]
    queue = collections.deque([node])  # We put the current vertex, and the current color
    while queue:
        vertex = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                path.append(neighbour)  # Remember that we were here
                queue.append(neighbour)  # Adding a neighbor to then walk out of it
    return path
