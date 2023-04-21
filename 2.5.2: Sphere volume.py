# assign the value of pi
pi = 3.14159

# initialize sphere_volume to 0.0
sphere_volume = 0.0

# get input for sphere_radius
sphere_radius = float(input())

# calculate the sphere volume using the formula
sphere_volume = (4.0 / 3.0) * pi * (sphere_radius ** 3)

# output the sphere volume with 2 decimal places
print(f'Sphere volume: {sphere_volume:.2f}')
