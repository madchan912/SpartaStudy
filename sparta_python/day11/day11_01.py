# 보물 1026
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0

for i in range(N):
    # 가장 작은 값과 큰 값을 곱해서 최솟값을 구함
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)