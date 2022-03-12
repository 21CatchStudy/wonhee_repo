# https://www.acmicpc.net/problem/2667

# 단지 형성 조건 찾기
# 형성 시 방문처리 => 1하고 총 1의 개수 세기

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

