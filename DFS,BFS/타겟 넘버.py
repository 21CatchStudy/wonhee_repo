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



def dfs(x, y, numbers, target):
    n = len(numbers)
    cnt = 0
    if x == n:
        if y == target:
            return 1
        else:
            return 0
    cnt += dfs(x+1, y+numbers[x], numbers, target)
    cnt += dfs(x+1, y-numbers[x], numbers, target)
    return cnt

def solution(numbers, target):
    answer = dfs(0, 0, numbers, target)
    return answer






from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
# stack을 이용한 dfs여도 마찬가지!
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer