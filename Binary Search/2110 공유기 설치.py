# https://www.acmicpc.net/problem/2110

def check(houses,distance):
    current = houses[0]
    cnt = 1
    for house in houses:
        if house - current >= distance:
            cnt+=1
            current = house
    return cnt

import sys
input = sys.stdin.readline
N, C = map(int,input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
min_d,max_d = 0,houses[-1]-houses[0]
while min_d<=max_d:
    d = (min_d+max_d)//2
    if check(houses,d)>=C: # 공유기 개수가 같거나 많을 시 거리를 늘려야 함
        ans = d
        min_d=d+1
    else: # 공유기 개수가 작을 시 거리를 줄여야함
        max_d = d-1
print(ans)

# import sys
#
# n, c = map(int, sys.stdin.readline().split())
# x = [int(sys.stdin.readline()) for _ in range(n)]
#
# x.sort()
# start = x[0]
# end = x[-1] - x[0]
# result = 0
#
# def binary_search(x, start, end):
#     while start <= end:
#         mid = (start+end)//2
#         now = x[0]
#         cnt = 1
#         for i in range(1, len(x)):  # 앞집부터 공유기 설치
#             if x[i] >= now + mid:
#                 cnt += 1
#                 now = x[i]
#         if cnt >= c:  # 주어진 공유기 개수보다 더 설치된다면
#             global result
#             start = mid + 1  # 설치 거리 늘리기
#             result = mid
#         else:
#             end = mid - 1
#
# binary_search(x, start, end)
# print(result)