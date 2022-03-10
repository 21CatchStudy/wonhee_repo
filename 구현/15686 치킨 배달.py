# https://www.acmicpc.net/problem/15686
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for row in range(n):
    city_info = list(map(int, input().split()))
    for column in range(n):
        if city_info[column] == 1:
            house.append((row, column))
        elif city_info[column] == 2:
            chicken.append((row, column))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
chicken_combination = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(chicken_combination):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        tmp = 1e9
        for cx, cy in chicken_combination:
            tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += tmp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for c in chicken_combination:
    result = min(result, get_sum(chicken_combination))

print(result)