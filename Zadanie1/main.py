import create_array
import create_population
import rate_population

# Create array
dataset = create_array.read_data("test.txt")
print(dataset)
size = (create_array.get_city_count(dataset))
arr = create_array.create_arr(dataset)
print(arr)

# Create population
pop = create_population.randomize_population(size, 10)
print(pop)

# Rate population
print(rate_population.rate_population(arr, pop))