# N과 K 입력받기
n, k = map(int, input().split())
coins = []  # 입력 받을 코인 저장할 리스트 생성
result = 0  # 동전 개수의 최솟값 결과
coin_cnt = 0

# N개의 줄에 동전 입력 받기
for i in range(n):
    coins.append(input())

# coins.sort()가 원하는 대로 작동하지 않음  =>  int형이 아닌 string형이기 때문 => coin.append(int(input())이면 정상 작동
for coin in coins[::-1]:  # 따라서 뒤에서 부터 출력하여 sort()역할을 대신
    if int(coin) > k:  # 주어진 k원보다 coin의 값이 크다면 무시
        continue
    else:  # coin은 str형이므로 python의 특징을 살려 int형으로 감싸 형변환
        coin_cnt = k // int(coin)  # 주어진 돈을 코인의 값으로 나눈 몫 = 사용된 코인의 개수
        result += coin_cnt  # 사용된 코인의 개수만큼 최종 값에 추가
        k %= int(coin)  # 주어진 값은 코인의 값만큼 나눈 후의 

print(result)