# https://www.acmicpc.net/problem/9461
'''
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
'''

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(1, 98):
    dp[i+3] = dp[i]+dp[i+1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])

