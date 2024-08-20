# 버블 소트 시간초과가 계속 나서 답을 확인했습니다...
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    # 듀플로 저장
    arr.append((int(input()), i))

sorted_arr = sorted(arr)
answer = []

for i in range(n):
    # 현재위치로 오기까지 걸리는 횟수의 나열
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)