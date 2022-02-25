n = int(input())
times = []
result = 0

for i in range(1, n+1):
    times.append(input())

'''
times 첫번째 원소 끝나는 숫자 확인
그 후에 오는 숫자는 무조건 끝숫자보다 커야한다.
시작과 끝 시간의 텀이 작은 것부터 차례대로 선택
'''
t_idx = []
for time in times:
    split_time = time.split(' ')
    for t in split_time:
        t_idx.append(t)
        start_time = t_idx.index()
        # start_time = list(map((lambda x: x % 2 == 0), t))
        # print(start_time)
        # t_idx.append(t)
        # if t_idx % 2 == 0:
        #     print(t_idx)
        # if split_time[t] % 2 != 0:
        #     start_time# 인덱스가 홀수번째
        # print(start_time)
#     if split_time[0] < split_time[1]:
#         continue
#
# print(result)

'''
LIS - dp (dynamic programming)
백준 - 전봇대
'''