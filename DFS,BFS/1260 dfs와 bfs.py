# https://www.acmicpc.net/problem/1260
# n, m, v = map(int, input().split())
# graph = []
# visited = [False] * (n+1)
# for i in range(m):
#     graph.append(list(map(int, input().split())))
#
# # dfs
# def dfs(graph, v, visited):
#     visited[v] = True  # 현재 노드를 방문 처리
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# # bfs
# from collections import deque
#
# def bfs(graph, v, visited):
#     # 큐 구현을 위해 deque라이브러리 사용
#     queue = deque([v])
#     visited[v] = True  # 현재 노드를 방문 처리
#     # 큐가 빌때까지 반복
#     while queue:
#         v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
#         print(v, end=' ')
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#
# print(dfs(graph, v, visited))
# print(bfs(graph, v, visited))

#
# n, m, v = map(int, input().split())
# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# for i in range(len(graph)):
#     graph[i].sort()
#
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
#             visited[i] = True
#
# from collections import deque
#
# def bfs(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#
# print(dfs(v))
# print(bfs(v))
#

# n, m, v = map(int, input().split())
# visited = [False] * (n + 1)
#
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# for i in range(len(graph)):
#     graph[i].sort()
#
#
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
#             visited[i] = True
#
# from collections import deque
#
# def bfs(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#
#
# print(dfs(v))
# visited = [False] * (n + 1)
# print(bfs(v))
#
#
# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [[False] * (n+1)]

# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(v)
#             visited[i] = True
#
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
#             visited[i] = True
#
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(v)
#             visited[i] = True

from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

from collections import deque

# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] * (n+1)
#
# # for i in range(len(graph)):
# #     graph[i].sort()
#
# def DFS(v):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             DFS(i)
#             visited[i] = True
#
# from collections import deque
#
# def BFS(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#
# print(DFS(v))
# visited = [False] * (n+1)
# print(BFS(v))



# from collections import deque
#
# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# visited = [False] * (n+1)
#
# for i in range(len(graph)):
#     graph[i].sort()
#
# def DFS(v):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             DFS(i)
#             visited[i] = True
#
# def BFS(v):
#     visited[v] = True
#     q = deque([v])
#     while q:
#         now = q.popleft()
#         print(now, end=' ')
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#
#
# print(DFS(v))
# visited = [False] * (n+1)
# print(BFS(v))






n, m, v = map(int, input().split())
visited = [False] * (n + 1)  # 노드 방문 정보를 입력할 리스트 표현

graph = [[] for _ in range(n + 1)]  # 노드에 입력될 정보 리스트 범위 설정

# 각 노드 연결 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


# dfs
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

# bfs
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

print(dfs(v))
visited = [False] * (n + 1)  # dfs, bfs 각각 표현해줘야 하므로 방문처리 초기화
print(bfs(v))


















