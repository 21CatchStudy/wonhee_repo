n = int(input())
data = list(map(int, input().split()))
result = 1

data.sort()
for i in data:
    if i <= result:  # 추들이 만들 수 있는 합보다 큰 수 중 최소값
        result += i

print(result)
