# https://www.acmicpc.net/problem/2206
from collections import deque

n, m = map(int, input().split())
map_info = []
for i in range(n):
    map_info.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def empty_room():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

    while q:
        x, y, c = q.popleft()  # 좌표와 벽을 부술 수 있는 남은 횟수
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내에 있다면
                if map_info[nx][ny] == '1' and c == 1:  # 벽을 하나 부숨
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])  # c를 -1해서 저장
                elif map_info[nx][ny] == '0' and visited[nx][ny][c] == 0:  # 빈방인 경우
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append([nx, ny, c])
    return -1
print(empty_room())