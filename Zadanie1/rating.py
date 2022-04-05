# Rate individual -> number
def rate_p(values_array: list, p: list):
    rating = 0
    for i in range(len(p)-1):
        x = p[i]
        y = p[i+1]
        rating += values_array[x][y]
    x = values_array[p[-1]][p[0]]
    rating += values_array[p[-1]][p[0]]
    return rating


# Rate population -> list[number]
def rate_population(arr:list, population:list):
    population_rating = []
    for i in range (len(population)):
        rating = rate_p(arr, population[i])
        population_rating.append(rating)
    return population_rating
