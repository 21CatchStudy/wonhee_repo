# # https://www.acmicpc.net/problem/2667
# from collections import deque
#
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     cnt = 1
#     q = deque()
#     q.append((x, y))
#     graph[x][y] = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             elif graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 q.append((nx, ny))
#                 cnt += 1
#     return cnt
#
# result = 0
# house = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             house.append(bfs(i, j))
#             result += 1
#
# print(result)
# house.sort()
# for k in house:
#     print(k)
# from collections import deque
#
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# visited = [0] * (n+1)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     cnt = 1
#     q = deque()
#     q.append((x, y))
#     graph[x][y] = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#             elif graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 q.append((nx, ny))
#                 cnt += 1
#     return cnt
#
# result = 0
# house = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             house.append(bfs(i, j))
#             result += 1
#
# print(result)
# print(house)
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

result = 0
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append(bfs(i, j))
            result += 1

print(result)
for i in sorted(house):
    print(i)
