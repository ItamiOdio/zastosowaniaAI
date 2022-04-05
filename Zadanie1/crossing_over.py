import random
def pmx_cross(parent1, parent2):

    size = len(parent1)
    break1 = random.randint(1, size - 2)
    break2 = random.randint(break1 + 1, size - 1)

    child1 = [-1] * len(parent1)
    child2 = [-1] * len(parent1)

    child1[break1:break2] = parent1[break1:break2]
    child2[break1:break2] = parent2[break1:break2]

    for i in range (0, size):
        if i < break1 or i > break2-1:
            child1[i] = pmx_loop(parent2, i, child1, child2)
            child2[i] = pmx_loop(parent1, i, child2, child1)

    # print(parent1)
    # print(parent2)
    # print()
    # print(child1)
    # print(child2)
    # print()
    # print(break1)
    # print(break2)

    return child1, child2


def pmx_loop(parent, index, child1, child2):
    val = parent[index]
    while (val in child1):
        # print(f'{val} już jest')
        val_index = child1.index(val)
        val = child2[val_index]

    return val


def cross(population, k):
    for i in range (0, len(population), 2):
        r = random.random()
        if r < k:
            # print (i)
            # print (r)
            try:
                children = pmx_cross(population[i], population[i+1])
                population[i] = children[0]
                population[i+1] = children[1]
            except IndexError:
                pass
            continue

    return population