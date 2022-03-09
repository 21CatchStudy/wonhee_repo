# https://www.acmicpc.net/problem/3190

n = int(input())
k = int(input())
for _ in range(k):
    row, column = map(int, input().split())
L = int(input())
for _ in range(L):
    x, c = input().split()

x, y = 0, 0
direction = ['U', 'D', 'L', 'R']
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
snake_len = 1

while True:



    if dx > n and dy > n:
        break