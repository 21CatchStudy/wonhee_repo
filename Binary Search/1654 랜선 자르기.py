# https://www.acmicpc.net/problem/1654

'''
4 11
802
743
457
539
'''

# k, n = map(int, input().split())
# LAN = sorted([int(input()) for _ in range(k)])
#
# start, end = 1, max(LAN)
#
#
# while start <= end:
#     mid = (start + end) // 2
#     line_cnt = 0
#     for i in LAN:
#         line_cnt += i // mid
#     if line_cnt >= n:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)


import sys

k, n = map(int, input().split())  # 랜선의 개수 K, 그리고 필요한 랜선의 개수 N
LAN = sorted([int(sys.stdin.readline()) for _ in range(k)])
start, end = 1, max(LAN)

while start <= end:
    mid = (start + end) // 2
    line_cnt = 0
    for i in LAN:
        line_cnt += i // mid
    if line_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

import sys

k, n = map(int, sys.stdin.readline().split())
LAN = sorted([int(sys.stdin.readline()) for _ in range(k)])

start, end = 1, max(LAN)

while start <= end:
    line_cnt = 0
    mid = (start + end)//2
    for i in LAN:
        line_cnt += i // mid
    if line_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

