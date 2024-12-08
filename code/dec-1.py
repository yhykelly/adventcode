import pandas as pd
import numpy as np
import csv
import collections

first = []
second = []

with open('input-dec1.csv', 'r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        ids = lines[0].split('   ')
        first.append(int(ids[0]))
        second.append(int(ids[1]))

counter_second = collections.Counter(second)
print(counter_second)
similarity_list = []
for item in first:
    if item in counter_second:
        frequency = counter_second[item]
        similarity_list.append(frequency)
    else:
        similarity_list.append(0)
        
print((similarity_list))
similarity_array = np.multiply(np.array(similarity_list), first)
print(np.sum(similarity_array))

# first star
first_arr = np.array(sorted(first))
second_arr = np.array(sorted(second))
diff = np.absolute(first_arr- second_arr)
sum = np.sum(diff)
print(sum)