import sys,heapq
input = sys.stdin.readline

n, k = map(int, input().split())
quests = []
totalExp = 0

for quest in map(int, input().split()):
	totalExp += quest
	heapq.heappush(quests, quest)

expLoss = 0
sol = 0
for _ in range(k):
	expLoss += heapq.heappop(quests)
	sol += totalExp - expLoss

print(sol)