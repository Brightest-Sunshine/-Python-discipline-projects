The first laboratory work in a cycle on the subject of User Interface Development

# Graph Rendering

This is a student project in which it is necessary to implement algorithms for breadth-first search and depth-first search on graphs, as well as their rendering. Programming language is Python 3.7

## Installation

In order for our program to work after downloading, you must additionally install a third-party library. To download, follow this link [Graphviz](https://graphviz.org/download/). When installing, add the path to graphviz in PATH

## Results of the program
Two graph traversal algorithms were implemented in the process. Each time the program is run, a new random graph is always generated with the number of vertices not exceeding 10. Then the steps begin to be drawn depending on which algorithm is selected. In the breadth-first graph traversal, each layer is marked with its own specific color.

```python
  # Algorithms.DFS(graph, visited, 0)
    Algorithms.BFS(graph, visited, 0)
```
![Создание графа](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_0.JPG)

We start the algorithm from the zero node.

![Шаг 1](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_1.JPG)

Next, we fill in the second layer, all those nodes that can be accessed from the zero vertex.

![Шаг 2](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_2.JPG)
![Шаг 3](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_3.JPG)
![Шаг 4](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_4.JPG)
![Шаг 5](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_5.JPG)

All the vertices of the second layer were bypassed. The next layer is the third.

![Шаг 6](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_6.JPG)

## Development team
1. Mamaeva Anastasia
2. Vedenichev Dmitry

