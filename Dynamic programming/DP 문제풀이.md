### Dynamic programming (동적 계획법)

**정의**

- 동적계획법 (DP)

  - 입력 크기가 작은 **부분들을 해결**한 후, **해당 부분 문제의 해를 활용**해서, **보다 큰 크기의 부분 문제를 해결**, **최종적으로 전체 문제를 해결**하는 알고리즘

  - **상향식 접근법**으로, **가장 최하위 해답**을 구한 후, 이를 저장하고, **해당 결과값을 이용해서 상위 문제**를 풀어가는 방식

- Memoization 기법을 사용함

  - Memoization : 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술

- 문제를 잘게 쪼갤 때, 부분 문제는 중복되어, 재활용 됨



1. [BOJ] 피보나치 함수 / 실버 3

> https://www.acmicpc.net/problem/1003

**고려한 점**

<u>코드 작성 패턴</u>

1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기

- `print`를 찍다 보니 
  - 0의 개수 ➡ `dp[i]`
  - 1의 개수 ➡ `dp[i] + dp[i - 1]` 임을 확인
- n이 0, 1인 경우에는 범위 오류로 인해 따로 `zero`, `one` 값을 지정

**코드**

```python
# 1. 빈리스트 만들기 (입력값에 따른)
dp = [0]*41  
# 2. 초기값을 설정
dp[1] = 1
dp[2] = 1
dp[3] = 2

# 3. 점화식 기반으로 계산값 적용하기
for i in range(4, 41):
    dp[i] = dp[i-1] + dp[i-2]

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        zero, one = 1, 0
    elif n == 1:
        zero, one = 0, 1
    while n > 1:
        for i in range(n):
            zero = dp[i]
            one = dp[i] + dp[i - 1]
        break
    # 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
    print(zero, one)
```

**개선해야할 점**

- 얻어걸린 코드라 다른 방식을 더 생각해봐야할 것 같음

```python
# 탐욕법 풀이
t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)
```

----------------------------------

2. [BOJ] 계단 오르기 / 실버 3

> https://www.acmicpc.net/problem/2579

**고려한 점**

- 코드 작성 패턴

- 솔루션 도출 시 그림 그려서 이해하는 것이 도움이 되었음

![img](https://blog.kakaocdn.net/dn/cQlb4F/btq0YhonhNU/RqL8rBdhD3GST28YkA5JC1/img.png)

(출처 : https://jainn.tistory.com/83)

**코드**

```python
n = int(input())
stairs = [0]  # 시작점은 계단에 포함되지 않는다.
for _ in range(n):
    stairs.append(int(input()))

# 1. 빈리스트 만들기 (입력값에 따른)
dp = [0]*301
# 2. 초기값을 설정
if n == 1:
    print(stairs[n])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    # 3. 점화식 기반으로 계산값 적용하기
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    # 4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
    print(dp[n])
```

**개선해야할 점**

- dp는 상향식 접근이므로 작은 부분을 먼저 해결 한 후 전체 문제를 해결하는 알고리즘

------------------------------------

3. [BOJ] 포도주 시식 / 실버 1

> https://www.acmicpc.net/problem/2156

**고려한 점**

- 코드 작성 패턴
- 2번 문제인 계단오르기와 유사한 문제

```python
# 오답 부분
for i in range(3, n+1):
    dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])

# 수정 후
for i in range(3, n):
    dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])

참고 : https://www.acmicpc.net/board/view/60664
```

- 계단 오르기 문제는 마지막 계단을 꼭 밟고 끝나지만, 포도주 시식 문제는 마지막 잔을 마시지 않을 수도 있다

  - `dp[i]` ➡ i번째 포도주까지 최대로 마신 포도주의 양

  **고려해야 하는 조건**

  - `dp[i-2]+wine[i]` ➡ i번째 포도주를 마시고 i-2번째 까지 마신 양
  - `dp[i-3]+wine[i-1]+wine[i]` ➡ i, i-1번째를 포도주를 마시고, i-3번째까지 마신 양
  - ✔`dp[i-1]` ➡ i번째를 마시지 않은 경우의 i-1번째 포도주까지 마신 양

**코드**

```python
n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0]*1001
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])
print(max(dp))
```

**개선해야할 점**

- 조건을 잘 살피고 더 생각해보기

-----------------------------------

4. [BOJ] 평범한 배낭 / 골드 5

> https://www.acmicpc.net/problem/12865

**고려한 점**

- 솔루션 도출 하지 못해서 참고 사이트와, 유튜브 강의 시청
  - 유튜브 : https://www.youtube.com/watch?v=uggO0uzGboY
  - 참고 : https://myjamong.tistory.com/319

![img](https://blog.kakaocdn.net/dn/twX4d/btriopBG0aZ/63pb7TM4pfyj8TwnIhtqL0/img.png)

**코드**

```python
n, k = map(int, input().split())  # 물품의 수 N, 버틸 수 있는 무게 K
dp = [0]*(k+1)

# 유튜브 설명 코드
for _ in range(n):
    w, v = map(int, input().split())  # 물건의 무게 W, 물건의 가치 V
    if w > k:
        continue
    for j in range(k, 0, -1):
        if j + w <= k and dp[j] != 0:
            dp[j+w] = max(dp[j+w], dp[j] + v)
        dp[w] = max(dp[w], v)
print(max(dp))


# 참조 설명 코드
for _ in range(n):
    w, v = map(int, input().split())  # 물건의 무게 W, 물건의 가치 V
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])
```

- 해당 위치의 최대 가치 `dp[j]`
- 들어갈 물건의 무게 `w`만큼 이전의 최대 가치`dp[j-w]` 에 물건의 가치 `v`를 더한 값 
  - 두개의 값 중 최대값 
  - 물건이 들어간 상태의 무게가 누적된다고 생각

**개선해야할 점**

- 솔루션 도출시 이해가 안된다면 한개씩 찍어보기
- 점화식 만들기
