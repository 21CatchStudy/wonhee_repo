# https://www.acmicpc.net/problem/12015
'''
6
10 20 10 30 20 50
'''
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

array = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:  # 모든 원소 비교
            array[i] = max(array[i], array[j]+1)
print(max(array))

'''
## 진호님 코드
import sys
input =  sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))

max_lists = []

# lower bound 
# target값 보다 같거나 큰 가장 작은 인덱스
def idx_check(arr,target):
    lo ,hi = 0, len(arr)-1
    while lo <= hi:
        m = (lo+hi)//2
        if arr[m] >= target:
            hi = m-1
        else:
            lo = m+1
    # len(arr)
    return lo

for number in n_list:
    idx = idx_check(max_lists,number)
    if idx == len(max_lists):
        max_lists.append(number)
    else:
        max_lists[idx] = number

print(len(max_lists))
'''

'''
## 상문님 코드
LIS 알고리즘
순차 탐색
'''