# https://www.acmicpc.net/problem/1003
'''
3
0
1
3
'''
'''
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
'''


dp = [0]*41
dp[1] = 1
dp[2] = 1
dp[3] = 2

for i in range(4, 41):
    dp[i] = dp[i-1] + dp[i-2]


# n = int(input())
# if n == 0:
#     a, b = 1, 0
# elif n == 1:
#     a, b = 0, 1
# while n > 1:
#     for i in range(n):
#         a = dp[i]
#         b = dp[i]+dp[i-1]
#     break
# print(a, b)



t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        a, b = 1, 0
    elif n == 1:
        a, b = 0, 1
    while n > 1:
        for i in range(n):
            a = dp[i]
            b = dp[i] + dp[i - 1]
        break
    print(a, b)
'''
t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)
'''
