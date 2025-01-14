import numpy as np

# # Create one variable to store safe reports to
number_of_safe_reports = 0

def is_safe_report(report):
  if (all(i < j and j - i <= 3 for i, j in zip(report, report[1:])) or all(i > j and i - j <= 3 for i, j in zip(report, report[1:]))):
    return True

  return False

def recursive_report_safety_check(report):
  flag = False
  for idx, data in enumerate(report):
    removed_element = report.pop(idx)
    flag = is_safe_report(report)
    if (flag):
      break
    report.insert(idx, removed_element)

  return flag

def the_problem_dampener(report):
  increase = False
  decrease = False
  same_number = False
  is_safe = is_safe_report(report)
  for idx, data in enumerate(report):
    if (idx == len(report) - 1):
      continue

    if (not(increase)):
      increase = np.sign(report[idx+1] - data) == 1
    if (not(decrease)):
      decrease = np.sign(report[idx+1] - data) == -1
    if (not(same_number)):
      same_number = np.sign(report[idx+1] - data) == 0

    if (same_number):
      is_safe = recursive_report_safety_check(report)
      break
    if (increase and (decrease or same_number)):
      is_safe = recursive_report_safety_check(report)
      break
    if (decrease and (increase or same_number)):
      is_safe = recursive_report_safety_check(report)
      break
    if (increase and report[idx+1] - data > 3):
      is_safe = recursive_report_safety_check(report)
      break
    if (decrease and report[idx+1] - data < -3):
      is_safe = recursive_report_safety_check(report)
      break

  return is_safe

# Open the file in read mode
with open('input.txt', 'r') as file:
  # Read each line in the file
  for line in file:
    report = line.split()
    report = list(map(int, report))

    # Safe increasing report or safe decreasing report
    if (is_safe_report(report)):
      number_of_safe_reports += 1
    elif (the_problem_dampener(report)):
      number_of_safe_reports += 1

print('Number of safe reports with the problem dampener is:', number_of_safe_reports)