n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        if A[i][j] != B[i][j]:
            print()
'''
3 4
0000
0010
0000
1001
1011
1001
-----
2
'''