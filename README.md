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
    third_graph = Graph.GraphBuilder.create_from_file(path_to_file)
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
    from graph import Algorithms, Graph, GifMaker
    graph = Graph.GraphBuilder.create_random_directed_graph()
    functions = [Algorithms.DFS, Algorithms.BFS]
    for fun in functions:
        random_node = random.randint(0, graph.count_nodes - 1)
        gif = Algorithms.gif(graph, random_node, fun)
        GifMaker.save(gif, path_to_save)
```

### Graph rendering
```python
    from graph import Graph
    graph = Graph.Graph(0, {0: []})
    graph.add_edge(1, 0)
    graph.draw_graph(graph)
```
The latest version added gif creation from the command line.
Runs from the project folder
```commandline
    python -m graph.Graph -h //Для помощи
    python -m graph.Graph --input_file graph/examples/data/graph_1.txt
    python -m graph.Graph --input_file graph/examples/data/graph_1.txt --output_file my_graph_gif

```
***

# Development team
1. Mamaeva Anastasia

     work email: mamaeva.as@edu.spbstu.ru
    
2. Vedenichev Dmitry

     work email: vedenichev.da@edu.spbstu.ru 
