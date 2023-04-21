# Read integers from user input
user_num = int(input())
div_num = int(input())

# Compute quotient using floor division
quotient = user_num // div_num

# Output quotient 3 times using floor division
print(quotient, end=' ')
print(quotient // div_num, end=' ')
print(quotient // div_num // div_num)
