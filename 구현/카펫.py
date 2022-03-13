def solution(brown, yellow):
    answer = []
    result = []
    x, y = 0, 0

    total = brown + yellow
    for i in range(1, total + 1):
        if total % i == 0:
            answer.append(i)
    answer.remove(1)
    answer.remove(total)

    for i in answer:
        if len(answer) == 1:
            x = i
            y = i
        else:
            x = (answer[len(answer) // 2])
            y = (answer[(len(answer) // 2) - 1])
    result.append(x)
    result.append(y)

    return result


def solution(brown, yellow):
    total = brown + yellow
    result = []
    for i in range(1, total + 1 // 2):
        if total % i == 0:
            tmp = total // i
            x = tmp
            y = i

            tmp_total = x * 2 + (y - 2) * 2
            if tmp_total == brown:
                result.append(x)
                result.append(y)
                break
    return result