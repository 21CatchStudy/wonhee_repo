def solution(people, limit):
    answer = 0
    cnt = 0
    total = 0

    people.sort()

    for i in range(len(people)):
        total = people[i] + people[i - 1]

        if total >= 100:
            cnt += 1
        else:
            continue

    return cnt

def solution(people, limit):
    answer = 0
    cnt = 0
    total = 0

    people.sort()

    for i in range(len(people)-1):
        total = people[i] + people[i+1]
        if total >= 100:
            cnt += 1
        else:
            # if people[i] > 50:
            #     cnt += 1

    return cnt




def solution(people, limit):
    answer = 0
    cnt = 0

    people.sort()

    start, end = 0, len(people) - 1

    while start <= end:
        cnt += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return cnt