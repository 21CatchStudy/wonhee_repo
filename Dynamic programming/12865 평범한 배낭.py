# https://www.acmicpc.net/problem/12865

'''
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기

4 7
6 13
4 8
3 6
5 12
'''
n, k = map(int, input().split())  # 물품의 수 N, 버틸 수 있는 무게 K
dp = [0]*(k+1)

for _ in range(n):
    w, v = map(int, input().split())  # 물건의 무게 W, 물건의 가치 V
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])


# ## https://www.youtube.com/watch?v=uggO0uzGboY
# for _ in range(n):
#     w, v = map(int, input().split())  # 물건의 무게 W, 물건의 가치 V
#     if w > k:
#         continue
#     for j in range(k, 0, -1):
#         if j + w <= k and dp[j] != 0:
#             dp[j+w] = max(dp[j+w], dp[j] + v)
#         dp[w] = max(dp[w], v)
# print(max(dp))


