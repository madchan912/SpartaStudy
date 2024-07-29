# 패션왕 신해빈 9375
import sys
input = sys.stdin.readline

test_case = int(input())


for _ in range(test_case):
    clothes = {}
    n = int(input().strip())

    for _ in range(n):
        # 옷의 이름과 종류를 키,밸류로 딕셔너리에 저장
        name, type = input().strip().split()
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]
    count = 1

    # 각 옷의 종류에서 입는 가능 수는 갯수 + 안 입는 경우 1 해서 +1
    for i in clothes:
        count *= (len(clothes[i]) + 1)

    print(count - 1)