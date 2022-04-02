# https://www.acmicpc.net/problem/2579
'''
6
10
20
15
25
10
20
'''

n = int(input())
stairs = [int(input()) for _ in range(n)]
total = 0

for stair in stairs:
    total += stair
    for i in range(3):
