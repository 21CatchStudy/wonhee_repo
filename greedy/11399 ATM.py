n = int(input())
p = list(map(int, input().split()))
time = 0
result = 0

p.sort()
for i in p:
    time += i
    result += time
    continue
print(result)