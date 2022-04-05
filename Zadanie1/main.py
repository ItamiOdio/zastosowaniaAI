import create_array
import create_population
import rating
import selection
import crossing_over
import mutation
import time


start_time = time.time()
# Create array
dataset = create_array.read_data("a280.txt")
print("Odczytane dane:")
print(dataset)
size = (create_array.get_city_count(dataset))
value_matrix = create_array.create_arr(dataset)
print("Macierz wartości:")
print(value_matrix)

# Create population
print("Populacja:")
population = create_population.randomize_population(size, 200)
#random_pop = create_population.randomize_population(size, 300000)
print(population)

# Rate population
print("Ocena populacji (podglądowo, wykorzystana w selekcji):")
print(rating.rate_population(value_matrix, population))

generation = 0
while generation < 3000:

    cp = 0.2
    mp = 0.04

    # Selection
    #print("Populacja po selekcji:")
    population = selection.tournament_selection(40, population, value_matrix)
    #print(selected_population)

    # Cross-over
    cr = crossing_over.cross(population, cp)

    #Mutation
    cr = mutation.mutate(generation, 2500, cr, mp)

    #print(cr)
    if generation%100==0:
        print(min(rating.rate_population(value_matrix, population)))

    generation +=1

population_rating = rating.rate_population(value_matrix, population)
print()
final_rating = min(population_rating)
final_index = population_rating.index(final_rating)
print(final_rating)
print ('-'.join(str(x) for x in population[final_index]))
print()
#random_rate = min((rating.rate_population(value_matrix, random_pop)))

print("--- %s seconds ---" % (time.time() - start_time))
#print(random_rate)