# https://gurumee92.tistory.com/164

def solution(NUM, number):
    arr = [[]] + [[int(str(NUM) * i)] for i in range(1,9)]

    if [number] in arr:
        return arr.index([number])

    for i in range(2, 9):
        for j in range(1, i):
            for a in arr[j]:
                for b in arr[i-j]:
                    arr[i].append(a + b)
                    arr[i].append(a * b)
                    arr[i].append(a - b)
                    if 0 != b:
                        arr[i].append(a // b)
        if number in arr[i]:
            return i
        arr[i] = list(set(arr[i]))

    return -1

def solution(N, number):
    dp = [[]]
    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    temp.append(k + l)
                    if k - l >= 0:
                        temp.append(k - l)
                    temp.append(k * l)
                    if l != 0 and k != 0:
                        temp.append(k // l)
        temp.append(int(str(N) * i))
        if number in temp:
            return i
        dp.append(list(set(temp)))

    return -1


def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break

        DP.append(numbers)

    return answer


def solution(N, number):
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # 3. n 일반화
    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer


def solution(N, number):
    dp = [0]
    for i in range(1, 9):
        dp.append({int(str(N)*i)})
    for i in range(1, 9):
        for j in range(1, i):
            # print(i, j, i-j)
            # set은 순서가 없기 때문에 list로 바꿔서 for해야하는 줄 알았는데
            # 이런 방법으로 set내부의 모든 원소에 쉽게 접근할 수 있다. dict도 마찬가지 이다.
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    dp[i].add(num1*num2)
                    if num2 != 0:
                        dp[i].add(num1//num2)
        if number in dp[i]:
            return i
    return -1


# https: // junha1125.github.io / blog / ubuntu - python - algorithm / 2020 - 0
# 9 - 20 - N_express /