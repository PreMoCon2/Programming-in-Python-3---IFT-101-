# Prompt user to input three floating-point numbers
x = float(input())
y = float(input())
z = float(input())

# Compute and output x to the power of z
power1 = x ** z

# Compute and output x to the power of (y to the power of z)
power2 = x ** (y ** z)

# Compute and output the absolute value of (x minus y)
abs_value = abs(x - y)

# Compute and output the square root of (x to the power of z)
sqrt_value = (x ** z) ** 0.5

# Output the results
print(f'{power1:.2f} {power2:.2f} {abs_value:.2f} {sqrt_value:.2f}')
