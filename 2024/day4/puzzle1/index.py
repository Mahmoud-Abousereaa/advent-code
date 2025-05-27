word = 'XMAS'
word_length = len(word)
word_count = 0

def similar_vertical_index_letter(data, letter_idx):
# Collect similar index letters, stopping after 4
  equivalent_letters = []
  stripped_data = [s.strip() for s in data]
  for string in stripped_data:
    if len(equivalent_letters) < 4:
      equivalent_letters.append(string[letter_idx])

  return equivalent_letters

def similar_diagonal_index_letter(data, letter_idx, diagonal = ''):
# Collect similar index letters, stopping after 4
  equivalent_letters = []
  stripped_data = [s.strip() for s in data]
  data_length = len(next(iter(stripped_data)))
  prev_letter_idx = -1

  for string in stripped_data:
    if (prev_letter_idx == letter_idx):
      continue
    if len(equivalent_letters) < 4:
      prev_letter_idx = letter_idx
      equivalent_letters.append(string[letter_idx])
    if (letter_idx > 0 and diagonal == 'LEFT'):
      prev_letter_idx = letter_idx
      letter_idx -= 1
    if (letter_idx < data_length - 1 and diagonal == 'RIGHT'):
      prev_letter_idx = letter_idx
      letter_idx += 1

  return equivalent_letters

def horizontal_lookup(line, letter_idx):
  count = 0
  if (word_length + letter_idx <= len(line)):
    count += 1 if (line[letter_idx:(letter_idx + word_length)] == word) else 0
  if (letter_idx + 1 - word_length >= 0):
    count += 1 if (line[letter_idx + 1 -word_length:(letter_idx + 1)][::-1] == word) else 0

  return count

def vertical_lookup(lines, line_idx, letter_idx):
  count = 0
  if (line_idx >= word_length - 1):
    equivalent_letters = similar_vertical_index_letter(lines[line_idx+1-word_length:line_idx+1][::-1], letter_idx)
    count += 1 if (''.join(equivalent_letters) == word) else 0
  if (line_idx - word_length <= len(lines)):
    equivalent_letters = similar_vertical_index_letter(lines[line_idx:line_idx+word_length], letter_idx)
    count += 1 if (''.join(equivalent_letters) == word) else 0
  return count

def diagonal_lookup(lines, line_idx, letter_idx):
  count = 0
  if (line_idx >= word_length - 1):
    equivalent_letters = similar_diagonal_index_letter(lines[line_idx+1-word_length:line_idx+1][::-1], letter_idx, 'LEFT')
    count += 1 if (''.join(equivalent_letters) == word) else 0

    equivalent_letters = similar_diagonal_index_letter(lines[line_idx+1-word_length:line_idx+1][::-1], letter_idx, 'RIGHT')
    count += 1 if (''.join(equivalent_letters) == word) else 0
  if (line_idx - word_length <= len(lines)):
    equivalent_letters = similar_diagonal_index_letter(lines[line_idx:line_idx+word_length], letter_idx, 'LEFT')
    count += 1 if (''.join(equivalent_letters) == word) else 0

    equivalent_letters = similar_diagonal_index_letter(lines[line_idx:line_idx+word_length], letter_idx, 'RIGHT')
    count += 1 if (''.join(equivalent_letters) == word) else 0
  return count

content = open('input.txt', 'r')
lines = content.readlines()

# Read each line in the file
for index, line in enumerate(lines):
  line = line.strip()
  for idx, c in enumerate(line):
    if (c == 'X'):
      word_count += horizontal_lookup(line, idx)
      word_count += vertical_lookup(lines, index, idx)
      word_count += diagonal_lookup(lines, index, idx)

print('word_count', word_count)