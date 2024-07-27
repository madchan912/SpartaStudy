# 국회의원 선거 1417
import sys,heapq
input = sys.stdin.readline

n = int(input())
dasom = -int(input())
vote = []
cnt = 0

# 다솜의 투표를 제외한 나머지를 heap에 저장 -로 저장
for _ in range(n - 1):
    num = int(input())
    heapq.heappush(vote, -num)

# -로 저장된 값을 최소 비교해서 다솜이가 제일 커질때 까지 while
while vote:
    num = heapq.heappop(vote)
    if dasom >= num:
        num += 1
        dasom -= 1
        cnt += 1
        heapq.heappush(vote, num)

print(cnt)