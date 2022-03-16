# # https://www.acmicpc.net/problem/2606
#
# computer = int(input())
# pair = int(input())
# graph = [[] for _ in range(computer+1)]
# for i in range(pair):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# visited = [False] * (computer+1)
# cnt = 0
#
#
# def dfs(v):
#     global cnt
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
#             cnt += 1
#
# dfs(1)
# print("dfs방식 :",cnt)
#
# from collections import deque
#
# def bfs(v):
#     global cnt
#     q = deque([v])
#     visited[v] = True
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True
#                 cnt += 1
#
# bfs(1)
# print("bfs방식 :",cnt)


from collections import deque

computer = int(input())
pair = int(input())
graph = [[] for _ in range(computer+1)]

for i in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer+1)
cnt = 0

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True
            cnt += 1
    return cnt

print(dfs(1))

def bfs(v):
    global cnt
    visited[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

print(bfs(1))
