# https://www.acmicpc.net/problem/14503
n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = x + dy[direction]

    if d[nx][ny] == 0 and data[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)