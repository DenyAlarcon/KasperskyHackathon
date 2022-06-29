import sys

data = sys.stdin.readlines()

out_arr = []
curr_arr = []
count = 0

for line1 in data:
    for line2 in data:
        if line1 == line2:
            continue
        for i in range(len(line1)):
            if line1[i] == line2[i]:
                curr_arr.append(line2[i])
                if i == len(line1) - 1:
                    out_arr = curr_arr
                    curr_arr = []
                    count = 0
            else:
                count = count + 1
                if count > 1:
                    count = 0
                    curr_arr = []
                    break
print(''.join(out_arr))

# import sys
#
# data = sys.stdin.readlines()
#
# out_arr = []
# curr_arr = []
# count = 0

# for line1 in data:
#     for line2 in data:
#         if line1 == line2:
#             continue
#         for i in range(len(line1)):
#             if line1[i] == line2[i]:
#                 curr_arr.append(line1[i])
#                 if i == len(line1) - 1:
#                     out_arr = curr_arr
#                     curr_arr = []
#                     count = 0
#             else:
#                 count = count + 1
#                 if count > 1:
#                     count = 0
#                     curr_arr = []
#                     break
# print(''.join(out_arr))

