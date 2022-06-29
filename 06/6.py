import sys

data = sys.stdin.readlines()

N = int(data[0])
data = data[1:]
arr = [[0] * N for i in range(N)]
count = 0

for i in range(0, N):
    line = "".join(data[i].split(" "))
    for j in range(0, N):
        arr[i][j] = int(line[j])

for i in range(0, N):
    for j in range(0, N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            count = count + 1
            for l in range(j+1, N):
                if arr[i][l] == 1:
                    arr[i][l] = 0
                    for k in range(i + 1, N):
                        if arr[k][l] == 1:
                            arr[k][l] = 0
                        else:
                            break
                else:
                    break
            for k in range(i+1, N):
                if arr[k][j] == 1:
                    arr[k][j] = 0
                    for l in range(j + 1, N):
                        if arr[k][l] == 1:
                            arr[k][l] = 0
                        else:
                            break
                else:
                    break

print(count)