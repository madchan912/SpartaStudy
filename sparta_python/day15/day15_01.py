# 침투 13565
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    # 지나간 길을 true 바꿈
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny)

m, n = map(int, sys.stdin.readline().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().rstrip())))

visited = [[False] * n for i in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for y in range(n):
    if graph[0][y] == 0 and not visited[0][y]:
        dfs(0, y)

# 마지막 줄에 true가 1개라도 있다면 y = 0에서부터 내려온 true
if True in visited[m-1]:
    print('YES')
else:
    print('NO')