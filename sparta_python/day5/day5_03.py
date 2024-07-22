# # 숫자 카드 10815
import sys
input = sys.stdin.readline

n = int(input())
cards = input().split()
m = int(input())
checks = input().split()

answer = {}

# answer 딕셔너리에 키 -> 카드 종류 , 밸류는 0으로 생성
for i in range(n):
    answer[cards[i]] = 0

# 해당 딕셔너리 안에 checks의 카드가 있으면 1 없으면 0 출력
for j in range(m):
    if checks[j] in answer:
        print(1, end=' ')
    else:
        print(0, end=' ')