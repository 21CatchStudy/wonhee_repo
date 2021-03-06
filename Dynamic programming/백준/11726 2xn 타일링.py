# https://www.acmicpc.net/problem/11726

'''
점화식 : 이웃하는 두개의 항 사이에 성립하는 관계를 나타낸 관계식
- dp[n+3] = dp[n+1] + dp[n+2]
- dp[n] = dp[n-1] + dp[n-2]
- 가장 적은 경의의 수부터 계산을 해본 후, 패턴을 찾아, (점화)식을 세우기
'''
'''
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
'''
n = int(input())
# 1. 빈리스트 만들기
dp = [0]*1001
# 2. 초기값 설정
dp[1] = 1
dp[2] = 2
# 3. 점화식 기반으로 계산값 적용하기
for index in range(3, 1001):
    dp[index] = dp[index-1] + dp[index-2]
# 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
print(dp[n]%10007)

'''
전체 코드
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for index in range(3,1001):
    dp[index] = dp[index-1] + dp[index-2]
print(dp[n] % 10007)
'''