import imageio
import os


FORMAT = '.gif'
FORMAT_POSITION = 0  # Where in the file name is the type (BFS, DFS)
DELIMITER = "_"  # What separates the parameters in the file name?
GIF_SPEED = 0.5


def make_gif_from_files(file_names, path):  # get file names(png), create gif file.
    file_loc = path + gif_name(path, file_names[0]) + FORMAT
    print(file_loc)
    with imageio.get_writer(file_loc, mode='I', duration=GIF_SPEED) as writer:  # create gif from files
        for file_name in file_names:
            image = imageio.imread(file_name)
            writer.append_data(image)
    print("Finish ", file_loc)


def gif_name(path, file):  # find out type of gif and how many of this type we already have
    elem = file.split(DELIMITER)
    type_of_gif = elem[FORMAT_POSITION]
    return type_of_gif + DELIMITER + str(count_same_types(path, type_of_gif))


def count_same_types(path, type_of_gif):  # count how many files of this type exist in our directory +1
    files = os.listdir(path=path)
    count = 1
    for file in files:
        spl = file.split(DELIMITER)
        if spl[FORMAT_POSITION] == type_of_gif:
            count += 1
    return count
