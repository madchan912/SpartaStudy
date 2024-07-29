# 최소 힙 1927
import sys, heapq
input = sys.stdin.readline

N = int(input())
x = []
answer = 0
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(x,num)
    else:
        if len(x) == 0:
            print(0)
        else:
            answer = heapq.heappop(x)
            print(answer)