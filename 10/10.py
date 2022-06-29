data = input()

letters = "".join(set(data.lower()))
letters = ''.join(sorted(letters))
arr = []

for letter in letters:
    data1 = data
    data1 = data1.replace(letter, "")
    data1 = data1.replace(letter.upper(), "")
    i = -1
    while len(data1) > 0:
        i = i + 1
        if i == len(data1)-1:
            break
        if data1[i].lower() == data1[i+1].lower():
            data1 = data1[0:i] + data1[i+2:]
            i = i - 2
    arr.append(len(data1))

print(min(arr))

