The first laboratory work in a cycle on the subject of User Interface Development
***
# Graph Rendering

This is a student project in which it is necessary to implement algorithms for breadth-first search and depth-first search on graphs, as well as their rendering. Programming language is Python 3.7
***
## Installation

In order for our program to work after downloading, you must additionally install a third-party library. To download, follow this link [Graphviz](https://graphviz.org/download/). When installing, add the path to graphviz in PATH
***
## Installing dependencies

To connect all the dependencies, you need to write in the terminal
```python
   pip install -r requirement.txt
```
***
## Results of the program
In the process, two graph traversal algorithms were implemented. Each time the program is run, a new random graph with a maximum of 10 vertices is always generated. Then the steps start to be drawn depending on which algorithm is selected. The results appear in a separate folder named "BFS_result" or "DFS_result". After that, gifs are created from the pictures obtained earlier.

### BFS GIF
![GIF_BFS](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/BFS_2.gif)

### DFS GIF
![GIF_DFS](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/DFS_2.gif)

***
## Examples of calling functions
### Graph creation
```python
    from graph import Graph
    graph = Graph.GraphBuilder.create_random_directed_graph() 
    another_graph = Graph.Graph(2, {1: [2], 2: []})
    graph.add_edge(1, 2)
```

### BFS
```python
    from graph import Algorithms, Graph
    graph = Graph.GraphBuilder.create_random_directed_graph()
    start_node_ind = 0
    path = Algorithms.BFS(graph, start_node_ind)
```

### DFS
```python
    from graph import Algorithms, Graph
    graph = Graph.GraphBuilder.create_random_directed_graph()
    start_node_ind = 0
    path = Algorithms.DFS(graph, start_node_ind)
```

### GIF creation
```python
    from graph import Algorithms, Graph
    graph = Graph.GraphBuilder.create_random_directed_graph()
    functions = [Algorithms.DFS, Algorithms.BFS]
    for fun in functions:
        random_node = random.randint(0, graph.count_nodes - 1)
        path = Algorithms.gif(graph, random_node, fun)
```

### Graph rendering
```python
    from graph import Graph
    graph = Graph.Graph(0, {0: []})
    graph.add_edge(1, 0)
    graph.draw_graph(graph)
```
***

# Development team
1. Mamaeva Anastasia

     work email: mamaeva.as@edu.spbstu.ru
    
2. Vedenichev Dmitry

     work email: vedenichev.da@edu.spbstu.ru 
