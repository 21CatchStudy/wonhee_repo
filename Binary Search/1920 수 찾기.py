# https://www.acmicpc.net/problem/1920

'''
5
4 1 5 2 3
5
1 3 7 9 5
'''

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_search(target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if n_list[mid] > target:
        return binary_search(target, start, mid - 1)
    elif n_list[mid] < target:
        return binary_search(target, mid + 1, end)
    else:
        return True

for i in m_list:
    if binary_search(i, 0, n-1):
        print(1)
    else:
        print(0)







# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))
#
#
# # # 시간 제한에 걸리는 코드
# # for i in m_list:
# #     if i not in n_list:
# #         print('0')
# #     else:
# #         print('1')
#
# '''
# m_list만큼 반복 후 각각의 아이템을 반복해서 n_list에서 i가 있는지 확인하는 반복
# M x N의 수행속도 이므로 시간 복잡도는 O(n^2)
# 반복문을 내부에서 한 번더 반복하므로
#
# 문제 핵심 : 시간 복잡도 낮추기 -> 일정 수준 이하로 만들기
# 해결 : 이진 탐색
# '''
#
# n_list.sort()  #1,2,3,4,5
#
# def binary_search(value, start, end):
#     if start > end:
#         return False
#
#     mid = (start + end)//2
#     if n_list[mid] > value:
#         return binary_search(value, start, mid - 1)
#     elif n_list[mid] < value:
#         return binary_search(value, mid + 1, end)
#     else:
#         return True
#
# for i in m_list:
#     if binary_search(i, 0, n-1):
#         print(1)
#     else:
#         print(0)
#
#
# '''
# O(logn) x m 와 유사한 시간 복잡도를 가짐
# '''