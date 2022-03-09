# https://www.acmicpc.net/problem/3190

n = int(input())
k = int(input())
map_info = [[0]*(n+1) for _ in range(n+1)]
dir_info = []

for _ in range(k):
    row, column = map(int, input().split())
    map_info[row][column] = 1

L = int(input())
for _ in range(L):
    x, c = input().split()
    dir_info.append((int(x), c))

# (동), 서, 남, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, C):
    if C == 'L':
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4
    return direction

def simulate():
    x, y = 1, 1  # 뱀 위치
    map_info[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0  # 처음에는 동쪽 보고 있음
    time = 0  # 시작 후 지난 시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and map_info[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if map_info[nx][ny] == 0:
                map_info[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                map_info[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if map_info[nx][ny] == 1:
                map_info[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == dir_info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, dir_info[index][1])
            index += 1
    return time

print(simulate())