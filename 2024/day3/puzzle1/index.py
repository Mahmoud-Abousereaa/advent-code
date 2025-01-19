import re
import math

# Create the regex pattern
pattern = r'mul\((\d{1,3},\d{1,3})\)'

# Read the file
content = open('./input.txt', 'r').read()

# Find all matches
matches = re.findall(pattern, content)

sum = 0
for idx, data in enumerate(matches):
  numbers = data.split(',')

  # Convert strings to integers
  number_array = [int(x) for x in numbers]
  multiplication_res = math.prod(number_array)
  sum += multiplication_res

print('The sum of adding up all of the results of the multiplications is:', sum)