import sys

data = sys.stdin.readlines()

first_line = data[0]
first_num = first_line[6:]
delta = 0
first_idx = 0
second_idx = -1
curr_idx1 = 0
curr_idx2 = -1

for line in data:
    curr_idx2 = curr_idx2 + 1
    second_num = line[6:]
    sub = int(second_num) - int(first_num)
    if sub > delta:
        first_idx = curr_idx1
        second_idx = curr_idx2
        delta = sub
        print(line)
        print("sub %d" % sub)
        print("delta %d" % delta)
    elif sub < 0:
        first_num = second_num
        curr_idx1 = curr_idx2

first_time = data[first_idx]
second_time = data[second_idx]
print("%s %s %d" % (first_time[0:5], second_time[0:5], delta))

