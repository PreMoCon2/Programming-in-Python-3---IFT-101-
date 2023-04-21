from collections import namedtuple

# Define a named tuple called Player with the fields name, number, position, and team
Player = namedtuple('Player', ['name', 'number', 'position', 'team'])

# Create instances of the Player named tuple for Cam Newton and Lebron James
cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')

# Print out information about each player using the attributes of the named tuple
print(f'{cam.name}(#{cam.number}) is a {cam.position} for the {cam.team}.')
print(f'{lebron.name}(#{lebron.number}) is a {lebron.position} for the {lebron.team}.')
