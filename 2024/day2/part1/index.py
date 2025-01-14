# Create one variable to store safe reports to
number_of_safe_reports = 0

# Open the file in read mode
with open('input.txt', 'r') as file:
  # Read each line in the file
  for line in file:
    report = line.split()
    report = list(map(int, report))
    # Safe increasing report or safe decreasing report
    if (all(i < j and j - i <= 3 for i, j in zip(report, report[1:])) or all(i > j and i - j <= 3 for i, j in zip(report, report[1:]))):
      number_of_safe_reports += 1

print(number_of_safe_reports)