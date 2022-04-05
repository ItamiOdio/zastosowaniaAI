import random

def inversion_mutation(individual):
    break1 = random.randint(1, len(individual) - 2)
    break2 = random.randint(break1 + 1, len(individual) - 1)
    individual = individual[0:break1] + individual[break2-1:break1-1:-1] + individual[break2:]

    return individual


def replacement_mutation(individual):
    breaks = random.sample(individual, 2)
    individual[breaks[0]], individual[breaks[1]] = individual[breaks[1]], individual[breaks[0]]
    return individual


def mutate (generation, change_gen, population, k):
    for i in range (len(population)):
        if random.random() < k:
            if generation < change_gen:
                mutated_ind = inversion_mutation(population[i])

            else:
                mutated_ind = replacement_mutation(population[i])

            population[i] = mutated_ind
    return population