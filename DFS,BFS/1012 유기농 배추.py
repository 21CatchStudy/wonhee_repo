# https://www.acmicpc.net/problem/1012

# from collections import deque
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     graph[x][y] = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             elif graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 q.append((nx, ny))
#
# t = int(input())
# for i in range(t):
#     n, m, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     for j in range(k):
#         x, y = map(int, input().split())
#         graph[x][y] = 1
#     result = 0
#     for a in range(n):
#         for b in range(m):
#             if graph[a][b] == 1:
#                 bfs(a, b)
#                 result += 1
#
#     print(result)

from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    ground[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if ground[nx][ny] == 1:
                ground[nx][ny] = 0
                q.append((nx, ny))


for a in range(t):
    n, m, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]

    for b in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)
