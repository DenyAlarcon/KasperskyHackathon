import sys

def get_length(d, fp, sp, length, friends):
    if fp not in friends:
        friends.append(fp)
    else:
        return -1
    if fp in d:
        persons = d[fp]
    else:
        return -1
    for person in persons:
        if person == sp:
            return length
        else:
            length = get_length(d, person, sp, length + 1, friends)
    return length

data = sys.stdin.readlines()

d = {}

for line in data:
    key, value = line.split()
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
# print(d)

pair = data[-1]

fp, sp = pair.split()

length = -1

friends = []
# sys.setrecursionlimit(4000)

print(get_length(d, fp, sp, length, friends))
