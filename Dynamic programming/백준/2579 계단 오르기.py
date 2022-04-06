# https://www.acmicpc.net/problem/2579
'''
6
10
20
15
25
10
20
'''
'''
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
'''
n = int(input())
stairs = [0]  # 시작점은 계단에 포함되지 않는다.
for _ in range(n):
    stairs.append(int(input()))

# 1. 빈리스트 만들기 (입력값에 따른)
dp = [0]*301
# 2. 초기값을 설정
if n == 1:
    print(stairs[n])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    # 3. 점화식 기반으로 계산값 적용하기
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    # 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
    print(dp[n])

