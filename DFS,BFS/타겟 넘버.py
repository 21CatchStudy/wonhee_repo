# DFS (재귀 활용)
def solution(numbers, target):
    answer = 0
    graph = [0]
    for num in numbers:
        num_lst = []
        for i in graph:
            num_lst.append(i + num)
            num_lst.append(i - num)
        graph = num_lst

    for j in graph:
        if j == target:
            answer += 1
    return answer



def dfs(l, s, numbers, target):
    n = len(numbers)
    cnt = 0
    if l == n:
        if s == target:
            return 1
        else:
            return 0
    cnt += dfs(l+1,s+numbers[l],numbers,target)
    cnt += dfs(l+1,s-numbers[l],numbers,target)
    return cnt

def solution(numbers, target):
    answer = dfs(0,0,numbers,target)
    return answer
