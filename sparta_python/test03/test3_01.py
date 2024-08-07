# 숨바꼭질 1697
import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    queue = deque([s])
    while queue:
        s = queue.popleft()
        if s == k:
            return visited[s]
        for i in(s - 1, s + 1, s * 2):
            if 0 <= i < MAX and not visited[i]:
                # 해당 위치에 기존 부모 위치의 횟수 + 1
                visited[i] = visited[s] + 1
                queue.append(i)

# 0 <= n <= 100,000
MAX = 100001
n, k = map(int, input().split())
visited = [0] * MAX

fast_time = bfs(n)

print(fast_time)