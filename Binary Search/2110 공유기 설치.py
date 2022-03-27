# https://www.acmicpc.net/problem/2110

import sys

n, c = map(int, sys.stdin.readline().split())
x = [int(sys.stdin.readline()) for _ in range(n)]

x.sort()
start = x[0]
end = x[-1] - x[0]
result = 0

def binary_search(x, start, end):
    while start <= end:
        mid = (start+end)//2
        now = x[0]
        cnt = 1
        for i in range(1, len(x)):  # 앞집부터 공유기 설치
            if x[i] >= now + mid:
                cnt += 1
                now = x[i]
        if cnt >= c:  # 주어진 공유기 개수보다 더 설치된다면
            global result
            start = mid + 1  # 설치 거리 늘리기
            result = mid
        else:
            end = mid - 1  

binary_search(x, start, end)
print(result)