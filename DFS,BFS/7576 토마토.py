# # https://www.acmicpc.net/problem/7576
# from collections import deque
#
# m, n = map(int, input().split())
# tomato = []
# for _ in range(n):
#     tomato.append(list(map(int, input().split())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# q = deque([])
# for i in range(n):
#     for j in range(m):
#         if tomato[i][j] == 1:
#             q.append([i, j])
#
#
# def bfs():
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             elif tomato[nx][ny] == 0:
#                 tomato[nx][ny] = tomato[x][y] + 1
#                 q.append([nx, ny])
#
# bfs()
# result = 0
# for i in tomato:
#     print(i)
#     for j in i:
#         if j == 0:
#             print(-1)
#             exit(0)
#     result = max(result, max(i))
# print(result-1)
from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

cnt = 1

def bfs():
    global cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))

bfs()
result = 0
is_zero = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            is_zero = 1
        result = max(result, tomato[i][j])

if is_zero == 1:
    print(-1)
else:
    print(result-1)
