def rate_p(arr: list, p: list):
    rating = 0
    for i in range(len(p)-1):
        x = p[i]
        y = p[i+1]
        rating += arr[x][y]
    return rating


def rate_population(arr:list, population:list):
    population_rating = []
    for i in range (len(population)):
        rating = rate_p(arr, population[i])
        population_rating.append(rating)
    return population_rating
