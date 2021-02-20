The first laboratory work in a cycle on the subject of User Interface Development

# Graph Rendering

This is a student project in which it is necessary to implement algorithms for breadth-first search and depth-first search on graphs, as well as their rendering. Programming language is Python 3.7

## Installation

In order for our program to work after downloading, you must additionally install a third-party library. To download, follow this link [Graphviz](https://graphviz.org/download/). When installing, add the path to graphviz in PATH

## Results of the program
In the process, two graph traversal algorithms were implemented. Each time the program is run, a new random graph with a maximum of 10 vertices is always generated. Then the steps start to be drawn depending on which algorithm is selected. The results appear in a separate folder named "BFS_result" or "DFS_result". 

### BFS
Consider the operation of the breadth-first traversal algorithm.
When the graph is first traversed by width, each layer is marked with its own specific color.

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

### DFS
We will also give an example of depth-first traversal of the graph.

```python
    Algorithms.DFS(graph, visited, 0)
  # Algorithms.BFS(graph, visited, 0)
```

Initially, the program generated the following graph:
![Инициализация графа](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_0.JPG)

We start the traversal from the zero top.
![Шаг_1](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_1.JPG)

We continue to go down lower and lower until there are peaks that we can get to.
![Шаг_2](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_2.JPG)
![Шаг_3](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_3.JPG)
![Шаг_4](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_4.JPG)
![Шаг_5](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_5.JPG)
![Шаг_6](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_6.JPG)

# Development team
1. Mamaeva Anastasia
2. Vedenichev Dmitry

