import sys
import io

arr1 = []
arr2 = []
arr3 = []
out_arr = []
count = 1

with io.open('dataset_267210_1.txt', encoding='utf-8') as file:
    for line in file:
        if int(line[11]) == 1:
            arr1.append("%d%s" % (count, line))
        elif int(line[11]) == 2:
            arr2.append("%d%s" % (count, line))
        else:
            arr3.append("%d%s" % (count, line))
        count = count + 1

for a in arr1:
    print(a)

for i in range(len(arr1)):
    line = arr1[i]
    ss1 = arr1[i]
    ss2 = arr1[i+1]
    ss1 = ss1[7:9]
    ss2 = ss2[7:9]
    if int(ss2) - int(ss1) > 3:
        out_arr.append(line[0])

for i in range(len(arr2)):
    line = arr2[i]
    ss1 = arr2[i]
    ss2 = arr2[i+1]
    ss1 = ss1[7:9]
    ss2 = ss2[7:9]
    if int(ss2) - int(ss1) > 3:
        out_arr.append(line[0])

for i in range(len(arr3)):
    line = arr3[i]
    ss1 = arr3[i]
    ss2 = arr3[i+1]
    ss1 = ss1[7:9]
    ss2 = ss2[7:9]
    if int(ss2) - int(ss1) > 3:
        out_arr.append(line[0])
# for i in range(len(arr)):
#     tid1 = arr[i]
#     tid1 = tid1[11]
#     ss1 = arr[i]
#     ss1 = ss2[6:7]
#     for j in range(i+1, len(arr)):
#         tid2 = arr[j]
#         tid2 = tid2[11]
#         if tid1 == tid2:
#             ss2 = arr[i]
#             ss2 = ss2[6:7]
#             if int(ss2)-int(ss1) > 3:
#                 out_arr.append(i+1)


