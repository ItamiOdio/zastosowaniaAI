import create_array
import create_population
import rating
import selection
import random

# Create array
dataset = create_array.read_data("test.txt")
print("Odczytane dane:")
print(dataset)
size = (create_array.get_city_count(dataset))
arr = create_array.create_arr(dataset)
print("Macierz wartości:")
print(arr)

# Create population
print("Populacja:")
pop = create_population.randomize_population(size, 10)
print(pop)

# Rate population
print("Ocena populacji (podglądowo, wykorzystana w selekcji):")
print(rating.rate_population(arr, pop))

#Selection
print("Populacja po selekcji:")
print(selection.tournament_selection(3, pop, arr))