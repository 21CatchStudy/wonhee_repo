# 음료수 얼려 먹기
''''
4 5
00110
00011
11111
00000
'''
n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 범위 벗어나면 종료
        return False
    if ice[x][y] == 0:  # 방문하지 않았다면
        ice[x][y] = 1  # 방문 처리
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)


























