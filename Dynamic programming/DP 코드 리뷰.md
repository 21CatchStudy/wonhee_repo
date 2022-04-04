[Jinho_repo]

#### 피보나치 함수

- `0`, `1`의 호출을 따로 구현하여 코드가 훨씬 간결해진 것 같습니다. 배워갑니다!

```python
dp[i][0] = dp[i-1][0] + dp[i-2][0]
dp[i][1] = dp[i-1][1] + dp[i-2][1]
```



#### 계단 오르기

- 경우의 수를 따로 적어주셔서 이해하기가 수월했습니다!

- 런타임 에러 원인이였던 인덱스 에러를 if-else문으로 해결할 수 있는 방법입니다.

```python
if n == 1:
    print(stairs[n])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[n])
```



#### 포도주 시식

- 현재 `i`의 위치에서 경우의 수를 직관적으로 적어주신것이 좋았습니다.

- 초기값 설정을 if문 활용해서 풀어내신 부분 배워갑니다!

```python
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
# 비교
for i in range(n):
    if i < 2:
        dp[i] = dp[i-1] + grapes[i]
```



#### 평범한 배낭

- 점화식 도출 명확하게 설명해주신 점 감사합니다! 





[minhyeok_repo]

#### 피보나치 함수

- dp의 상향식 접근법을 정확하게 이해하시고 푸신 것 같습니다!



#### 계단 오르기

- 주석을 잘 달아주셔서 이해하기 편했습니다. 감사합니다!



#### 포도주 시식

- 저도 3가지 조건 중 `dy[i-1]` 조건을 놓치고 있어서 틀렸었습니다. 다양한 조건을 생각하며 풀어야하는 것 같아요!



#### 평범한 배낭

- 점화식과 어느 부분이 틀렸고 수정했는지 설명해주셔서 좋았습니다.





[sangmun_repo]

#### 피보나치 함수

- 수정 후 코드는 탐욕법을 활용한 코드로 보입니다! DP 활용하여 푸신다면 dp에 대한 이해도가 더 오를것이라 생각됩니다!



#### 계단 오르기

- 저도 dp강의 들으면서 배운 dp코드 작성 패턴인데 참고하시면 좋을 것 같아서 적어두었습니다!

```
코드 작성 패턴
1. 빈리스트 만들기 (입력값에 따른)
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 추출하기
```



#### 평범한 배낭

- weight, value를 활용해서 점화식을 만들 수 있군요! 배워갑니다

```python
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])

# 비교
for _ in range(n):
    w, v = map(int, input().split())  
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])
```



#### 포도주 시식

- 저도 3가지 조건 중 `d[i-1]`조건을 생각하지 못해서 틀렸었습니다. 조건을 좀 더 살펴봐야겠습니다! 