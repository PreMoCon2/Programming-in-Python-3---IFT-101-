# prompt user to input the name, price, and quantity of a food item
item_name = input('Enter food item name:\n')
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))

# calculate the total cost of the item
item_total = item_price * item_quantity

# output an itemized receipt for the first item
print("\nRECEIPT")
print(f"{item_quantity} {item_name} @ ${item_price:.2f} = ${item_total:.2f}")
print(f"Total cost: ${item_total:.2f}")

# prompt user to input the name, price, and quantity of a second food item
item2_name = input("\nEnter second food item name:\n")
item2_price = float(input("Enter item price:\n"))
item2_quantity = int(input("Enter item quantity:\n"))

# calculate the total cost of the second item
item2_total = item2_price * item2_quantity

# output an itemized receipt for the second item
print("\nRECEIPT")
print(f"{item_quantity} {item_name} @ ${item_price:.2f} = ${item_total:.2f}")
print(f"{item2_quantity} {item2_name} @ ${item2_price:.2f} = ${item2_total:.2f}")
total_cost = item_total + item2_total
print(f"Total cost: ${total_cost:.2f}")

# add a 15% gratuity to the total cost and output the grand total
gratuity = total_cost * 0.15
total_with_tip = total_cost + gratuity
print(f"\n15% gratuity: ${gratuity:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
