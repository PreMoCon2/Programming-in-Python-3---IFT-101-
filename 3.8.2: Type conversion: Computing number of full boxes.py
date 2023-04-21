num_full_boxes = 0.0  # initialize the variable to keep track of the total number of full boxes

num_itemsA = int(input())  # get the number of items in group A from the user
num_itemsB = int(input())  # get the number of items in group B from the user
num_itemsC = int(input())  # get the number of items in group C from the user

# calculate the number of full boxes by adding up the number of items in each group and dividing by the box capacity
num_full_boxes = (num_itemsA + num_itemsB + num_itemsC) // 5

print(f'Number of full boxes: {int(num_full_boxes)}')  # output the number of full boxes as an integer
