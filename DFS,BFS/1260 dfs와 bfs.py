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

n, m, v = map(int, input().split())
visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

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
visited = [False] * (n + 1)
print(bfs(v))