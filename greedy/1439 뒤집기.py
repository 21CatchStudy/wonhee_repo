s = input()
make_0 = 0
make_1 = 0

for i in range(len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            make_1 += 1
        if s[i] == '1':
            make_0 += 1

result = min(make_0, make_1)
print(result)
