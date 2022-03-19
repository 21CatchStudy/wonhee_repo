# https://www.acmicpc.net/problem/10989

import sys

n = int(input())
check = [0]*10001

for i in range(n):
    data = int(sys.stdin.readline())
    check[data] = check[data] + 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)