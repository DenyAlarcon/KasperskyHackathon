import sys

# data = sys.stdin.readlines()
data = input()
# data = "480 USD 482631936 8709868"
ans = ""
print(data)
arr = data.split(" ")
print(arr)

if int(arr[0]) < 30:
    ans = 42302
elif 30 < int(arr[0]) < 90:
    ans = 42303
elif 91 < int(arr[0]) < 180:
    ans = 42304
elif 181 < int(arr[0]) < 365:
    ans = 42305
elif 365 < int(arr[0]) < 365*3:
    ans = 42306
elif int(arr[0]) > 365*3:
    ans = 42307

if arr[1] == "RUR":
    ans = str(ans) + str(810)
elif arr[1] == 'USD':
    ans = str(ans) + str(840)
elif arr[1] == 'EUR':
    ans = str(ans) + str(978)
elif arr[1] == 'GBP':
    ans = str(ans) + str(826)


ans = ans + "00000"
ans = ans + arr[3]

bik = arr[2]
bik = bik[6:9]

str1 = bik + ans
# str1 = "74640602810000000000025"
str2 = '71371371371371371371371'
# print(len(str1) == len(str2))
arrMult = []
for i in range(len(str1)):
    arrMult.append(int(str1[i]) * int(str2[i]))
# print(arrMult)
summ = 0
for i in range(len(arrMult)):
    if len(str(arrMult[i])) > 1:
        num = str(arrMult[i])
        # print(arrMult[i])
        arrMult[i] = num[-1:]
        # print(arrMult[i])
    summ = summ + int(arrMult[i])

summ = str(summ)
summ = summ[-1:]
summ = int(summ)*3
summ = str(summ)
K = summ[-1:]
ans = ans[0:8] + K + ans[9:]
# print(arrMult)
print(ans)