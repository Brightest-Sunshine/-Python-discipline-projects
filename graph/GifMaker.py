import imageio
import os

PATH = 'gifs\\'
FORMAT = '.gif'
FORMAT_POSITION = 0  # Where in the file name is the type (BFS, DFS)
DELIMITER = "_"  # What separates the parameters in the file name?
GIF_SPEED = 0.5


def make_gif_from_files(file_names):  # get file names(png), create gif file.
    file_loc = PATH + gif_name(file_names[0]) + FORMAT  # find out how this gif named
    with imageio.get_writer(file_loc, mode='I', duration=GIF_SPEED) as writer:  # create gif from files
        for file_name in file_names:
            image = imageio.imread(file_name)
            writer.append_data(image)
    print("Finish ", file_loc)
    return


def gif_name(file):  # find out type of gif and how many of this type we already have
    elem = file.split(DELIMITER)
    type_of_gif = elem[FORMAT_POSITION]
    return type_of_gif + DELIMITER + str(count_same_types(type_of_gif))


def count_same_types(type_of_gif):  # count how many files of this type exist in our directory
    files = os.listdir(path=PATH)
    count = 1
    for file in files:
        spl = file.split(DELIMITER)
        if spl[FORMAT_POSITION] == type_of_gif:
            count += 1
    return count
