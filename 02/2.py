import sys

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


data = sys.stdin.readlines()

arr_util = []

count = 0

for line in data:
   num = line[46:]
   arr_util.append(num)
arr_util = [int(line.rstrip()) for line in arr_util]
mean_num = mean(arr_util)
for util in arr_util:
    if (abs(util - mean_num) > mean_num/10):
        count = count + 1
print(count)

