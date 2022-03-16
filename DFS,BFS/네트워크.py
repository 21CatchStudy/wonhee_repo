visited = []
def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i)
            answer += 0
    return answer

def dfs(n, computers, v):
    global visited
    visited[v] = True

    for i in range(n):
        if not visited[i] and computers[v][i] == 1:
            dfs(n, computers, i)
            visited[i] = True


def solution(n, computers):
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)
                # DFS로 방문해준다.

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
            # 방문 처리하지 않은 마지막 까지 카운트.

    return answer


def solution(n, computers):
    from collections import deque
    not_visited = [True for _ in range(n)]

    cnt = 0
    while any(not_visited):  # True in not_visted
        Q = deque()
        alone = not_visited.index(True)
        Q.append(alone)
        not_visited[alone] = False
        cnt += 1
        while Q:
            current = Q.popleft()
            for i in range(n):
                if computers[current][i] and not_visited[i]:
                    not_visited[i] = False
                    Q.append(i)

    return cnt


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))]

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(i)

    for j in range(n):
        if not visited[j]:
            dfs(j)
            answer += 1

    return answer