# https://www.acmicpc.net/problem/11054

n = int(input())
a = list(map(int,input().split()))
reverse_a = a[::-1]

increase = [1 for i in range(n)]
decrease = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_a[i] > reverse_a[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(n)]
for k in range(n):
    result[k] = increase[k] + decrease[n-k -1]-1

print(max(result))


