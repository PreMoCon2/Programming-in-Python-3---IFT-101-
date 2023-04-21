# Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade,
# as well as the number of servings the recipe yields

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = int(input('How many servings does this make?\n'))

# Output the ingredients and serving size for the given amount of servings

print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_nectar_cups:.2f} cup(s) agave nectar")

# Prompt the user to specify the desired number of servings and adjust the amounts of each ingredient accordingly

desired_servings = int(input('\nHow many servings would you like to make?\n'))

lemon_juice_cups *= desired_servings / servings
water_cups *= desired_servings / servings
agave_nectar_cups *= desired_servings / servings

# Output the ingredients and serving size for the new amount of servings in cups

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_nectar_cups:.2f} cup(s) agave nectar")

# Convert the ingredient measurements to gallons and output the new amounts in gallons

lemon_juice_gallons = lemon_juice_cups / 16
water_gallons = water_cups / 16
agave_nectar_gallons = agave_nectar_cups / 16

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice_gallons:.2f} gallon(s) lemon juice")
print(f"{water_gallons:.2f} gallon(s) water")
print(f"{agave_nectar_gallons:.2f} gallon(s) agave nectar")
