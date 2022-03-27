# https://www.acmicpc.net/problem/10816
'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''
import sys

n = int(sys.stdin.readline())
n_num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_num = list(map(int, sys.stdin.readline().split()))


# 정답 코드 1
n_num.sort()

def binary_search(target, start, end):
    if start > end:
        return 0

    mid = (start + end)//2
    if n_num[mid] > target:
        return binary_search(target, start, mid - 1)
    elif n_num[mid] < target:
        return binary_search(target, mid + 1, end)
    else:
        return n_num[start:end+1].count(target)

n_dic = {}
for i in n_num:
    if i not in n_dic:
        n_dic[i] = binary_search(i, 0, n-1)

# print(n_dic) {-10: 2, 2: 1, 3: 2, 6: 1, 7: 1, 10: 3}

print(' '.join(str(n_dic[i]) if i in n_dic else '0' for i in m_num))

# 오답 코드
'''
for i in n_num:
    if binary_search(i, 0, n-1):
        print(n_num.count(i))
    else:
        print(0)
'''

# 정답 코드2
from collections import Counter
count = Counter(n_num)
# print(count) Counter({10: 3, -10: 2, 3: 2, 2: 1, 6: 1, 7: 1})

print(' '.join(str(count[i]) if i in count else '0' for i in m_num))

# 오답 코드2
'''
for i in m_num:
    if i in count:
        print(' '.join(str(count[i])), end=' ')
    else:
        print('0', end=' ')
'''