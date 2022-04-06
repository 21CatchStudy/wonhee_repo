# https://programmers.co.kr/learn/courses/30/lessons/42898

dp = [[0] * (m) for _ in range(n)]
dp[1][1] = 1

dx = [0, 1]
dy = [1, 0]

for x in range(1, n+1):
    for y in range(1, m+1):
        if [x, y] in puddles:
            dp[x][y] = 0
        else:
            dp[x][y] =
return (dp[n][m]) % 1000000007



def solution(m, n, puddles):
    answer = 0
    roadmap = [[0] * m for _ in range(n)]
    dx = [1, 0]
    dy = [0, 1]

    j = 0
    while [j + 1, 1] not in puddles and j in range(m):
        roadmap[0][j] = 1
        j += 1

    i = 0
    while[1, i + 1] not in puddles and i in range(n):
        roadmap[i][0] = 1
        i += 1

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] not in puddles:
                roadmap[i][j] = roadmap[i - 1][j] + roadmap[i][j - 1]

    return roadmap[-1][-1] % 1000000007



puddles = [[q, p] for [p, q] in puddles]
dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = 1

for x in range(1, n+1):
    for y in range(1, m+1):
        if x == 1 and y == 1:
            continue
        if [x, y] in puddles:
            dp[x][y] = 0
        else:
            dp[x][y] = (dp[x-1][j] + dp[x][y-1]) % 1000000007

return dp[n][m]


def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                continue
            if [x, y] in puddles:
                dp[x][y] = 0
            else:
                dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000007

    return dp[n][m]


dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = 1

for x in range(1, n+1):  # 0~3
    for y in range(1, m+1):  # 0~4
        if x == 1 and y == 1:
            continue
        elif [x, y] in puddles:
            dp[x][y] = 0
        else:
            dp[x][y] = dp[x][y-1] + dp[x-1][y]

return (dp[n][m] % 1000000007)

'''
오른쪽과 아래 
=> 1. 왼쪽
   2. 위쪽
    
dp[3][4] = dp[3][3], dp[2][4] => dp[x][y-1] + dp[x-1][y]
'''



def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for x in range(1, n+1):  # 0~3
        for y in range(1, m+1):  # 0~4
            if x == 1 and y == 1:
                continue
            elif [x, y] in puddles:
                dp[x][y] = 0
            else:
                dp[x][y] = dp[x][y-1] + dp[x-1][y]

    return (dp[n][m] % 1000000007)


# https://dev-note-97.tistory.com/141














