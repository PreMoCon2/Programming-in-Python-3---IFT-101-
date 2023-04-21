# Prompt user to input the amount to change
amount_to_change = int(input())

# Calculate the number of five-dollar bills by integer division
num_fives = amount_to_change // 5

# Calculate the number of one-dollar bills using the remainder operator %
num_ones = amount_to_change % 5

# Output the results
print('Change for $', amount_to_change)
print(num_fives, '$5 bill(s) and', num_ones, '$1 bill(s)')
