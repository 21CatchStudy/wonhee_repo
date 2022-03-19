# https://www.acmicpc.net/problem/11650

n = int(input())
data = []
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (x[0], x[1]))
for i in data:
    print(i[0], i[1])


n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

data.sort()
for i in range(n):
    print(data[i][0], data[i][1])