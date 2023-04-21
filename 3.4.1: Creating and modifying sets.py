male_names = { 'Oliver', 'Declan', 'Henry' }
name_to_remove = input()
name_to_add = input()

# Remove the specified name from the set
male_names.remove(name_to_remove)

# Add the new name to the set
male_names.add(name_to_add)

print(male_names)
