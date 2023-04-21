# Importing the math module to use pow() function
import math

# Prompting the user to input the initial key frequency
f0 = float(input())

# Computing r using the pow() function and the given formula
r = pow(2, 1/12)

# Computing the next 4 higher key frequencies using the formula fn = f0 * rn
f1 = f0 * pow(r, 1)
f2 = f0 * pow(r, 2)
f3 = f0 * pow(r, 3)
f4 = f0 * pow(r, 4)

# Outputting the initial frequency and the next 4 higher key frequencies
print(f'{f0:.2f} {f1:.2f} {f2:.2f} {f3:.2f} {f4:.2f}')
