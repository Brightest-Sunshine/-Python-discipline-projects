The first laboratory work in a cycle on the subject of User Interface Development

# Graph Rendering

This is a student project in which it is necessary to implement algorithms for breadth-first search and depth-first search on graphs, as well as their rendering. Programming language is Python 3.7

## Installation

In order for our program to work after downloading, you must additionally install a third-party library. To download, follow this link [Graphviz](https://graphviz.org/download/). When installing, add the path to graphviz in PATH

## Installing dependencies

To connect all the dependencies, you need to write in the terminal
```python
   pip install -r requirement.txt
```

## Results of the program
In the process, two graph traversal algorithms were implemented. Each time the program is run, a new random graph with a maximum of 10 vertices is always generated. Then the steps start to be drawn depending on which algorithm is selected. The results appear in a separate folder named "BFS_result" or "DFS_result". 

### BFS
Consider the operation of the breadth-first traversal algorithm.
When the graph is first traversed by width, each layer is marked with its own specific color.

```python
    from graphviz import Digraph
    from graph import Graph
    ...
  # Algorithms.DFS(graph, visited, 0)
    Algorithms.BFS(graph, visited, 0)
```
![Create_graph](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_0.JPG)

We start the algorithm from the zero node.

![Step_1](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_1.JPG)

Next, we fill in the second layer, all those nodes that can be accessed from the zero vertex.

![Step_2](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_2.JPG)
![Step_3](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_3.JPG)
![Step_4](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_4.JPG)
![Step_5](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_5.JPG)

All the vertices of the second layer were bypassed. The next layer is the third.

![Step_6](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/BFS_6.JPG)

### DFS
We will also give an example of depth-first traversal of the graph.

```python
    from graphviz import Digraph
    from graph import Graph
    ...
    Algorithms.DFS(graph, visited, 0)
  # Algorithms.BFS(graph, visited, 0)
```

Initially, the program generated the following graph:

![graph_initialization](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_0.JPG)

We start the traversal from the zero top.

![Step_1](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_1.JPG)

We continue to go down lower and lower until there are peaks that we can get to.

![Step_2](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_2.JPG)

![Step_3](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_3.JPG)

![Step_4](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_4.JPG)

![Step_5](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_5.JPG)

![Step_6](https://github.com/Brightest-Sunshine/-pictures-for-README-files/blob/master/pics/DFS_6.JPG)

# Development team
1. Mamaeva Anastasia
     work email: mamaeva.as@edu.spbstu.ru
     phone number: 8-987-615-01-94
2. Vedenichev Dmitry
     work email: vedenichev.da@edu.spbstu.ru 
