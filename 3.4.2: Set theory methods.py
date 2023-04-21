person1_cities = {'Edmonton', 'Vancouver', 'Paris', 'Bangkok', 'Bend', 'Boise', 'Memphis', 'Zurich', 'Accra', 'Cairo'}
person2_cities = {'Accra', 'Orlando', 'Tokyo', 'Paris', 'Anaheim', 'Buenos Aires', 'London', 'Lima', 'Seoul', 'Bangkok'}

# Use set methods to create sets all_cities, same_cities, and different_cities.
all_cities = person1_cities.union(person2_cities) # contains all the cities visited by both people
same_cities = person1_cities.intersection(person2_cities) # contains the cities visited by both people
different_cities = person1_cities.symmetric_difference(person2_cities) # contains the cities visited by either person1 or person2, but not both

print(sorted(all_cities))
print(sorted(same_cities))
print(sorted(different_cities))
