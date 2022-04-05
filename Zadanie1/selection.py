import rating
import random


def tournament_selection(k: int, population: list, values: list):
    n = len(population)
    ratings = rating.rate_population(values, population)
    # print(ratings)

    result = []
    for j in range(n):

        rnd_ind = random.sample(range(0, n), k)
        rnd_min = max(ratings)+1
        index_min = -1
        # print(rnd_ind)
        # print()
        for i in range(k):

            rnd = ratings[rnd_ind[i]]
            if rnd < rnd_min:
                rnd_min = rnd
                index_min = i
                # print(rnd)

        # print()
        # print(rnd_min)
        # print(index_min)
        # print(rnd_ind[index_min])
        result.append(population[rnd_ind[index_min]])

    #print(rating.rate_population(values, result))
    return result


def roulette_wheel_selection():
    pass

