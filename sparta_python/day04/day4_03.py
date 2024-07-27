# 할리갈리 27160
import sys
input = sys.stdin.readline

a = int(input())

# 할리갈리 카드 종류와 현재 갯수를 가지는 딕셔너리를 만듬
haligali = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM': 0
}

for i in range(a):
    fruit, count = input().split()
    # 입력값에 과일이 잇을 경우 해당 과일 카운트에 갯수만큼 추가
    if fruit in haligali:
        haligali[fruit] += int(count)

    # 카운트가 5인 경우 true로 확인
    # 단 마지막에 확인
    check = 5 in haligali.values()

if check : print('YES')
else:print('NO')