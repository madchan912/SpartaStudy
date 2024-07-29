# 크리스마스 선물 14235
import sys, heapq
input = sys.stdin.readline

n = int(input())
gift = []
left_gift = 0

for i in range(n):
    gifts = list(map(int,input().split()))

    # 0일때는 선물을 줌
    if gifts[0] == 0:
        # 현재 가지고 있는 선물이 없으면 0-1 출력
        if len(gift) == 0:
            print(-1)
        # 있으면 가장 가치있는(가장 큰수, 최소힙이므로 -로 집어넣은 최대값을 양수로 전환
        else:
            left_gift = -heapq.heappop(gift)
            print(left_gift)
        # 0이 아니면 push, 최대값을 구하는 최소힙이므로 -로 push
    else:
        for j in range(gifts[0]):
            heapq.heappush(gift, -gifts[j+1])