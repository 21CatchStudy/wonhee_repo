'''
3 3
3 1 2
4 1 4
2 2 2
-------
2

2 4
7 3 1 8
3 3 3 4
--------
3
'''
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    result = max(result, min_data)

print(result)