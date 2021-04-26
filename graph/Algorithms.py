"""
Algorithms.py
====================================
Module containing all graph algo i use in my Graph-rendering project
"""

import collections
from typing import Optional

from graph.Graph import Graph
from graph import GifMaker


def graph_pass_and_gif(graph: Graph, node: int, method, draw=False) -> list:
    """

    :param graph: graph:  class object: The graph in which to run method
    :param node: int: index of starting node
    :param method: function: method what used for visualisation
    :param draw: bool: Make step files during graph_pass_and_gif creation
    :return: list(imageio.class): result of imageio working with graph steps during method run

    """
    path = method(graph, node)
    gif_img = GifMaker.build_from_graph(graph, path, draw)
    return gif_img


def DFS(graph: Graph, node: int) -> set:
    """
    :param graph:  class object: The graph in which to run DFS
    :param node: int: index of starting node
    :return: visited: list: index of visited nodes, basically path

    """
    return __DFS(graph, node, set())


def __DFS(graph: Graph, node: int, visited: set) -> set:
    """
    :param graph: class object: The graph in which to run DFS
    :param visited: list: Numbers of visited nodes, basically path
    :param node: int: number of the current node
    :return visited: set: Numbers of visited nodes, basically path
    """
    if node not in visited:
        visited.add(node)
        for neighbour in graph.adjacency_list[node]:
            visited = __DFS(graph, neighbour, visited=visited)
    return visited


def BFS(graph: Graph, node: int) -> set:
    """
    :param graph:  class object: The graph in which to run BFS
    :param node: int: number of node from we run BFS
    :return: set[] path

    """

    visited = {node}
    path = {node}
    queue = collections.deque([node])  # We put the current vertex, and the current color
    while queue:
        vertex = queue.popleft()
        for neighbour in graph.adjacency_list[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                path.add(neighbour)  # Remember that we were here
                queue.append(neighbour)  # Adding a neighbor to then walk out of it
    return path
