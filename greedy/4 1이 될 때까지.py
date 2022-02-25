'''
25 5
-----
2

25 3
-----
6
'''
n, k = map(int, input().split())
cnt = 0

while n > 1:
    if n % k == 0:  # 나누어 떨어지는 경우
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)