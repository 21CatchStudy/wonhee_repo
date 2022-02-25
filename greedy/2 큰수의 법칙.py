'''
5 8 3
2 4 5 4 6
---------
46
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

# m번의 범위동안 반복하면서 k만큼 가장 큰 수 더하기
data.sort(reverse=True)
while m > 0:
    for i in range(k):
        result += data[0]
        m -= 1
    result += data[1]
    m -= 1

print(result)