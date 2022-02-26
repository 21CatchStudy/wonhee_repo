# n = int(input())
# times = []
#
# for _ in range(n):
#     start, end = map(int, input().split())
#     times.append([start, end])
#
# times = sorted(times, key=lambda x: x[0])
# times = sorted(times, key=lambda x: x[1])
#
# finish_time = 0
# count = 0
#
# for start, end in times:
#     if start >= finish_time:
#         count += 1
#         finish_time = end
#
# print(count)

'''
LIS - dp (dynamic programming)
백준 - 전봇대
'''

n = int(input())
times = []

for _ in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

time = sorted(times, key=lambda x: (x[0], x[1]))

finish_time = 0
cnt = 0

for start, end in time:
    if start > finish_time:
        cnt += 1
        finish_time = end

print(cnt)