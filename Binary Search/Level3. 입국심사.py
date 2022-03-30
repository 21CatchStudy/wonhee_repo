def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            # mid 시간 동안 심사 받은 사람 수
            people += mid // time
        if people >= n:  # 심사 받은 사람이 심사 받아야할 수보다 많다면 => 최적의 해
            answer = mid
            end = mid - 1
        elif people < n:
            start = mid + 1

    return answer