# Create two variables for the left hand side of the list and the right hand side of the list
left_hand_side_list = []
right_hand_side_list = []
distance_diff = []

# Open the file in read mode
with open('input.txt', 'r') as file:
  # Read each line in the file
  for line in file:
    # Print each line
    list = line.split()
    left_hand_side_item = list[::len(list)]
    right_hand_side_item = list[len(list)-1]
    left_hand_side_list.extend(left_hand_side_item)
    right_hand_side_list.append(right_hand_side_item)

# Iterate over the list and get the absolute difference between the left hand side and the right hand side
iterations = len(right_hand_side_list)
for idx in range(iterations):
  left_hand_side_list_min_item = min(left_hand_side_list)
  right_hand_side_list_min_item = min(right_hand_side_list)
  diff = int(left_hand_side_list_min_item) - int(right_hand_side_list_min_item)
  distance_diff.append(abs(diff))
  left_hand_side_list.remove(left_hand_side_list_min_item)
  right_hand_side_list.remove(right_hand_side_list_min_item)

print("The total distance between the lists is:", sum(distance_diff))