import imageio  # type: ignore
from graph import Graph

FORMAT = '.gif'
FORMAT_POSITION = 0  # Where in the file name is the type (BFS, DFS)
DELIMITER = "_"  # What separates the parameters in the file name?
GIF_SPEED = 0.5
PATH = 'steps/'


def build_from_graph(graph, path, draw=False):
    steps = []
    path_to_img = create_path(draw)
    gif_images = []
    for step in path:
        steps.append(step)
        img = Graph.Graph.draw_graph(graph, visited=steps, file_name=path_to_img(len(steps)))
        gif_images.append(imageio.imread(img))
    print("Collect data for gif", )
    return gif_images


def create_path(draw):
    if draw:  # to save steps.
        return lambda count: PATH + "Graph_" + str(count)
    else:
        return lambda count: "Graph"


def save(gif_images, path):
    imageio.mimsave(path + FORMAT, gif_images, fps=3)
    print("Save at " + str(path) + FORMAT)
