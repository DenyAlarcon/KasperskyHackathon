import sys

s = sys.stdin.readlines()

data = [i.split()[0:2] for i in s]

data

for i in range(len(data)):
    data[i].append(i+1)
    tm = data[i][0].split(':')
    sec = int(tm[0])*60*60 + int(tm[1])*60 + int(tm[2])
    data[i][0] = sec
data

n = len(data)

er = []

for i in range(n-1):
    for j in range(i+1,n):
        if (data[i][1] == data[j][1]):
            if (data[j][0] - data[i][0] >= 3):
                er.append(data[i][2])
            break
print(er)