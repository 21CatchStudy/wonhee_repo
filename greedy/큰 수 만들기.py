# 시간초과
from itertools import combinations

def solution(number, k):
    item = len(number) - k
    lst = []

    for i in combinations(number, item):
        join_i = "".join(i)
        lst.append(join_i)

    lst.sort()
    return lst[-1]
    ''' or
    return max(lst) 
    '''

from itertools import combinations

def solution(number, k):
    answer = ''
    number = list(map(''.join, combinations(number, len(number)-k)))
    return max(number)








'''
def solution(number, k):
    answer = [] # Stack

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
    '''