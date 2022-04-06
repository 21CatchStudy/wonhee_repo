# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0

    dp = [0] * 501
    dp[1] = triangle[0]
    dp[2] = max(triangle[1][0], triangle[1][1])
    for i in range(3, len(triangle)):
        dp[i] = max(dp[])
        ''' 
        하향식 접근
        triangle[1][0] -> triangle[2][0] or triangle[2][1]
        triangle[1][1] -> triangle[2][1] or triangle[2][2]
        triangle[1][2] -> triangle[1][2] or triangle[1][3]
        = > triangle[i - 1]
        
        상향식 접근
        triangle[4][2] -> triangle[3][1] or triangle[3][2] => triangle[x-1][y-1] or triangle[x-1][y]
        triangle[3][2] -> triangle[2][1] or triangle[2][2] => triangle[x-1][y-1] or triangle[x-1][y]
        triangle[2][2] -> triangle[1][1]  => triangle[x-1][y-1]
        triangle[1][0] -> triangle[0][0]  => triangle[x-1][y] 
        '''



    return answer

for x in range(1, len(triangle)):
    for y in range(i+1):
        if y == 0:
            triangle[x][y] += triangle[x-1][y]
        elif y == i:
            triangle[x][y] += triangle[x-1][y-1]
        else:
            triangle[x][y] += max(triangle[x-1][y], triangle[x-1][y-1]
return max(triangle[-1]))

# https://codedrive.tistory.com/49


def solution(triangle):
    for x in range(1, len(triangle)):  # 1부터 하는 이유 : 상향식 접근이므로 x-1씩 올라감. 0인 경우 x좌표 값이 -1이 되므로 1부터
        for y in range(x + 1):
            if y == 0:
                triangle[x][y] += triangle[x - 1][y]
            elif y == x:
                triangle[x][y] += triangle[x - 1][y - 1]
            else:
                triangle[x][y] += max(triangle[x - 1][y - 1], triangle[x - 1][y])

    answer = max(triangle[-1])
    return answer