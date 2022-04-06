# https://www.acmicpc.net/problem/2156
'''
6
6
10
13
9
8
1
'''
'''
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
'''
n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0]*1001
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])
print(max(dp))

# if n == 1:
#     print(wine[n])
# else:
#     dp[1] = wine[1]
#     dp[2] = wine[1] + wine[2]
#     for i in range(3, n+1):
#         dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])
#     print(dp[n])