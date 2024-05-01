from collections import Counter
from itertools import combinations

pokemon= ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']
names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
primary_types = ['Grass', 'Psychic', 'Dark', 'Bug', 'Rock']
secondary_types = ['Ice', None, None, None, 'Flying']
generations=[1, 1, 1, 5, 3]

# Combine all three lists secondary_types
names_types = [*zip(names,primary_types,secondary_types)]
print(*names_types, sep='\n')

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)


