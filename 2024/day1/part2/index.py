# Create two variables for the left hand side of the list and the right hand side of the list
left_hand_side_list = []
right_hand_side_list = []
similarity_score = []

# Open the file in read mode
with open('input.txt', 'r') as file:
  # Read each line in the file
  for line in file:
    # Print each line
    line_list = line.split()
    left_hand_side_item = line_list[::len(line_list)]
    right_hand_side_item = line_list[len(line_list)-1]
    left_hand_side_list.extend(list(map(int, left_hand_side_item)))
    right_hand_side_list.append(int(right_hand_side_item))

# Iterate over the list to check how many times and item appears on the right hand side list from the left hand side list
for idx, data in enumerate(left_hand_side_list):
  item_similarity_score = right_hand_side_list.count(data)
  similarity_score.append(data * item_similarity_score)

print("The lists similarity score is:", sum(similarity_score))