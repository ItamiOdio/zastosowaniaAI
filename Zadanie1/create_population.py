from random import shuffle


def randomize_p(x):
    p = []
    for i in range(x):
        p.append(i)
    shuffle(p)
    return p


def randomize_population(size: int, n: int):
    population = []
    for i in range(n):
        p = randomize_p(size)
        population.append(p)

    return population
