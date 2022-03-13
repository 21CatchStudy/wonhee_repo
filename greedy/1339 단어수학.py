# https://www.acmicpc.net/problem/1339
alpha_dict = {'A': 9, 'B': 4, 'C': 8, 'D': 6, 'E': 5, 'F': 3, 'G': 7}

n = int(input())
alpha = []
for _ in range(n):
    alpha.append(input())

res = []
for i in alpha:
    for j in i:
        if j == 'A':
            j = 9
            a = ''.join(j)
            print(a)


