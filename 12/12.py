import sys

data = sys.stdin.readlines()

N  = data.pop(0)
# print("N: " + N)

sea_map = []

for line in data:
    split_values = line.rstrip().split()
    # print(split_values)
    sea_map.append(split_values)

for i in range(int(N)):
    for j in range(int(N)):
        if sea_map[i][j] == '?':
            min_val = int(min(sea_map[i+1][j], sea_map[i][j+1], sea_map[i-1][j], sea_map[i][j-1]))
            max_val = int(max(sea_map[i+1][j], sea_map[i][j+1], sea_map[i-1][j], sea_map[i][j-1]))
            difference = max_val - min_val
            if difference <= 4:
                sea_map[i][j] = min_val + int(difference / 2)


for i in range(int(N)):
    for j in range(int(N)):
        if j != int(N) - 1:
            print("{0} ".format(sea_map[i][j]), end = '')
        else:
            print("{0}".format(sea_map[i][j]))
    # print("\n")
