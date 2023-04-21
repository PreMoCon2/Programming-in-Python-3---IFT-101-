# Initialize the variable avg_sales with 0
avg_sales = 0

# Read three integer inputs from the user and store them in the respective variables
num_sales1 = int(input())
num_sales2 = int(input())
num_sales3 = int(input())

# Calculate the average by adding the three numbers and dividing by 3, then assign it to avg_sales
avg_sales = (num_sales1 + num_sales2 + num_sales3) / 3

# Output the average with two decimal places
print(f'Average sales: {avg_sales:.2f}')
