import sys

def is_correct_path(d, begin, end, checkpoints):
    if begin not in checkpoints:
        checkpoints.append(begin)
    else:
        return "FALSE"
    if begin in d:
        sps = d[begin]
    else:
        return "FALSE"
    for sp in sps:
        if sp == end:
            return "TRUE"
        else:
            correctness = is_correct_path(d, sp, end, checkpoints)
            if correctness == "FALSE":
                return "FALSE"
            checkpoints.remove(sp)
            # return is_correct_path(d, sp, end, length + 1, checkpoints)

    return correctness

data = sys.stdin.readlines()

pair_to_check = data.pop(0)
begin, end = pair_to_check.split()

d = {}

for line in data:
    key, value = line.split()
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
# print(d)

checkpoints = []

print(is_correct_path(d, begin, end, checkpoints))
