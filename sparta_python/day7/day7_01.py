# 막대기 17608
import sys
input = sys.stdin.readline

stick = []
N = int(input())

# stick 리스트 생성
for _ in range(N):
    stick.append(int(input()))

count = 1 # 마지막 막대기는 무조건 보이므로
stick_last = stick[-1] # 마지막 막대기 크기

# 막대기를 뒤에서부터 순서대로 꺼내면서 비교
for i in reversed(range(N)):
    if stick[i] > stick_last:
        count += 1
        stick_last = stick[i]

print(count)