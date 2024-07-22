# 숫자 카드 2 10816
import sys
input = sys.stdin.readline

n = int(input())
cards = input().split()
m = int(input())
checks = input().split()

answer = {}

# 딕셔너리에서 키는 중복이 안되기때문에 밸류를 갯수로 생각해서 기본 1에
# 추가로 존재하면 +1을 하여 중복 카드 갯수를 셈
for card in cards:
    if card in answer:
        answer[card] += 1
    else:
        answer[card] = 1
# checks의 카드가 존재하면 해당 카드의 갯수만큼 출력 없으면 0 출력
for j in range(m):
    if checks[j] in answer:
        print(answer[checks[j]], end=' ')
    else:
        print(0, end=' ')