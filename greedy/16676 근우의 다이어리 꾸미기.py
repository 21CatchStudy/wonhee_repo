'''
1. 같은 수가 연속이라면, 같은 수 연속 개수만큼 스티커를 구매해야한다
2. 같은 수가 없다면, 한 장으로 해결 가능
'''
# n = int(input())
# sticker = 0
#
# str_n = str(n)
# list_n = []
#
# for i in str_n:
#     list_n.append(i)
#
# for j in list_n:
#     if list_n.count(j) == 1:
#         sticker = 1
#     else:
#         sticker = max(sticker, list_n.count(j))
#
# print(sticker)

n = input()
s = '1' * len(n)  # 문자의 길이만큼 구하기 위함

if len(n) == 1:
    print(1)
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n) - 1)
    
# 최적의 상태, 규칙성 존재, 다음 선택의 최적화와 같은가? => 그리디 고려