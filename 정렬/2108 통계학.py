# https://www.acmicpc.net/problem/2108

n = int(input())
data = sorted([int(input()) for _ in range(n)])

def one(data):
    return round(sum(data)/len(data))

def two(data):
    for i in range(len(data)):
        mid = i // 2
    return data[mid]

def three(data):
    from collections import Counter
    data_counter = Counter(data)
    mode = data_counter.most_common()
    m = mode[0][1]
    modes = []
    for i in mode:
        if i[1] == m:
            modes.append(i[0])
    if len(mode) > 1:
        return modes[1]
    elif len(data) == 1:
        for i in data:
            return i
    else:
        return modes[0]

def four(data):
    a = min(data)
    b = max(data)
    if len(data) == 1:
        return 0
    return abs(a) + b

print(one(data))
print(two(data))
print(three(data))
print(four(data))
