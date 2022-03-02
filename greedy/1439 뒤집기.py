s = input()
make_0 = 0  # 1을 0으로 만들기
make_1 = 0  # 0을 1로 만들기

for i in range(len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            make_1 += 1
        if s[i] == '1':
            make_0 += 1

result = min(make_0, make_1)
print(result)
