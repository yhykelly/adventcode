import csv

# problem 1
# list to save "safe", "unsafe" / true/false
checklist = []
SAFE = 'safe'
UNSAFE = 'unsafe'

safe_num = 0

with open('input-dec2.csv', 'r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        levels = line[0].split(' ') # each line
        levels_int = [int(item) for item in levels] # each line turned into integer
        strict_tendency = True # for the tendency of increase or decrease
        sign = None # for storing initial increase or decrease
        # check along each list
        for n in range(len(levels_int)-1):
            interval_diff = levels_int[n+1] - levels_int[n]
            if interval_diff == 0:
                strict_tendency = False
                break

            if sign is None:  # for the first record
                sign = 'decrease' if interval_diff < 0 else 'increase'

            if abs(interval_diff) > 3 or abs(interval_diff) < 1:
                strict_tendency = False
                break
            if (sign == 'decrease' and interval_diff > 0) or (sign == 'increase' and interval_diff < 0):
                strict_tendency = False
                break

        if strict_tendency:
            safe_num += 1

print(safe_num)

# problem 1 ends

# problem 2
checklist = []
SAFE = 'safe'
UNSAFE = 'unsafe'

safe_num_2 = 0

def check_safe(aList):
    strict_tendency = True 
    sign = None 
    for n in range(len(aList)-1):
        interval_diff = aList[n+1] - aList[n]
        if interval_diff == 0:
            strict_tendency = False
            break

        if sign is None:  # for the first record
            sign = 'decrease' if interval_diff < 0 else 'increase'

        if abs(interval_diff) > 3 or abs(interval_diff) < 1:
            strict_tendency = False
            break
        if (sign == 'decrease' and interval_diff > 0) or (sign == 'increase' and interval_diff < 0):
            strict_tendency = False
            break

    return strict_tendency

with open('input-dec2.csv', 'r')as file:
  csvFile = csv.reader(file)
  for line in csvFile:
        levels = line[0].split(' ') # each line
        levels_int = [int(item) for item in levels] # each line turned into integer
        if check_safe(levels_int):
            safe_num_2 += 1
            continue
        else:
            for i in range(len(levels_int)):
                left_one_out_list = levels_int[:i] + levels_int[i+1:] 
                if check_safe(left_one_out_list):
                    safe_num_2 += 1
                    break

print(safe_num_2)
        