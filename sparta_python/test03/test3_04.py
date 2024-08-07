# 빙산 2573
import sys
input = sys.stdin.readline

def dfs(x, y):
    for k in range(4):
        cnt = 0
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and ice[nx][ny] == 0:
            cnt += 1
        ice[x][y] -= cnt

n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for i in range(n):
    for j in range(m):
        if ice[i][j] != 0:
            dfs(i, j)