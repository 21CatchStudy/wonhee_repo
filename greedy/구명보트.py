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
        print(total)
        if total >= 100:
            cnt += 1
        else:
            if people[0] > 50:
                cnt += 1

    return cnt


def solution(people, limit):
    cnt_boat = 0
    people.sort()
    first, last = 0, len(people) - 1

    while first <= last:
        if people[first] + people[last] <= limit:
            first += 1
        last -= 1
        cnt_boat += 1

    return cnt_boat