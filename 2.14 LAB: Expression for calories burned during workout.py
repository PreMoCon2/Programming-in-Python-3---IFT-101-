# Get inputs for age, weight, heart rate, and time
age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())

# Compute the average calories burned
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368

# Output the result
print(f'Calories: {calories:.2f} calories')
