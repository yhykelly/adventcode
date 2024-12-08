import re

# regex pattern: 'mul\(\d+,\d+\)'

# muls = []
# muls_sum = 0

# with open('input-dec3.txt', 'r')as reader:
#   lines = reader.readlines()
#   for line in lines:
#     pattern = 'mul\(\d+,\d+\)'
#     mul = re.findall(pattern, line)
#     muls = muls + mul

# for item in muls:
#   pattern2 = '\d+,\d+'
#   digit_pair = re.findall(pattern2, item)
#   digit_pair_int = [int(n) for n in digit_pair[0].split(',')]
#   result = digit_pair_int[0] * digit_pair_int[1]
#   print(result)
#   muls_sum += result

# print("muls_sum = ",muls_sum )

# version 2 of part 1
# pattern_part1 = re.compile(r'mul\((\d+),(\d+)\)')
# muls_sum = 0
# with open('input-dec3.txt', 'r')as reader:
#   lines = reader.readlines()
#   for line in lines:
#     for match in pattern_part1.findall(line):
#         num1, num2 = map(int, match)
#         result = num1 * num2
#         muls_sum = muls_sum + result

# print(muls_sum)

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, open('input-dec3.txt').read())
res = 0
counted = True
for match in matches:
    if match == "do()":
        counted = True
    elif match == "don't()":
        counted = False
    else:
        if counted:
           print(match[4:-1])
           x, y = map(int, match[4:-1].split(","))
           res += x * y
print(res)

# part 2

# patter from do to don't = 'do\(\).+mul\((\d+),(\d+)\).+don't'

# part2 = 0
# pattern2 = "(don't\(\).*?)do\(\)"
# pattern2a = "don't\(\).*"
# pattern_part1 = re.compile(r'mul\((\d+),(\d+)\)')
# with open('input-dec3.txt', 'r')as reader:
#   lines = reader.readlines()
#   for line in lines:
#     no_dont_do_line = re.sub(pattern2, '', line)
#     print(no_dont_do_line)
#     print("***")
#     no_dont_line = re.sub(pattern2a, '', no_dont_do_line)
#     print(no_dont_line)
#     for match in pattern_part1.findall(no_dont_line):
#         print(match)
#         num1, num2 = map(int, match)
#         result = num1 * num2
#         part2 += result
# print("---")
# print(part2)