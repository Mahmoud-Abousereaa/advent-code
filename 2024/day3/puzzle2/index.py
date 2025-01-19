import re
import math

# Create the regex pattern
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

# Read the file
content = open('./input.txt', 'r').read()

# Find all matches
matches = re.findall(pattern, content)
sum = 0
do = True
for idx, data in enumerate(matches):
  print(data, do, sum)
  if (not(do) and data != "do()"):
    continue

  if (data == "don't()"):
    do = False
    continue

  if (data == "do()"):
    do = True
    continue

  numbers = re.findall(r'\d+', data)

  # Convert strings to integers
  number_array = [int(x) for x in numbers]
  multiplication_res = math.prod(number_array)
  sum += multiplication_res

print('The sum of adding up all of the results of the enabled multiplications is:', sum)