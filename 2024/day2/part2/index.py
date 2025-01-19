import numpy as np

# # Create one variable to store safe reports to
number_of_safe_reports = 0

def is_safe_report(report):
  if (all(i < j and j - i <= 3 for i, j in zip(report, report[1:])) or all(i > j and i - j <= 3 for i, j in zip(report, report[1:]))):
    return True

  return False

def apply_the_problem_dampener(report):
  flag = False
  for idx in enumerate(report):
    removed_element = report.pop(idx)
    flag = is_safe_report(report)
    if (flag):
      break
    report.insert(idx, removed_element)

  return flag

# Open the file in read mode
with open('input.txt', 'r') as file:
  # Read each line in the file
  for line in file:
    report = line.split()
    report = list(map(int, report))

    # Safe increasing report or safe decreasing report
    if (is_safe_report(report)):
      number_of_safe_reports += 1
    elif (apply_the_problem_dampener(report)):
      number_of_safe_reports += 1

print('Number of safe reports with the problem dampener is:', number_of_safe_reports)