import random
def pmx_cross(population: list):
    breaks = random.sample(range(2, len(population)-1), 2)
    print(breaks)

    pass

pmx_cross([[3, 4, 2, 0, 1], [4, 1, 3, 2, 0], [1, 4, 0, 2, 3], [3, 1, 4, 0, 2], [4, 0, 3, 1, 2], [0, 3, 2, 4, 1], [4, 0, 2, 1, 3], [0, 4, 3, 1, 2], [3, 4, 0, 1, 2], [0, 2, 3, 1, 4]])