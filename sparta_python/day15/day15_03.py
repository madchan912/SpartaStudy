# 음식물 피하기 1743
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 음쓰가 있으면 1
    count.append(1)
    trash[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < m and trash[ny][nx] == 1:
            dfs(ny, nx)

n, m, k = map(int, input().split())
trash = [[0] * m for _ in range(n)]
visited = [[False] * m for i in range(n)]

for _ in range(k):
    # 좌표가 순서여서 -1
    r,c = map(int, input().split())
    trash[r-1][c-1] = 1

count = []
area = []

for i in range(n):
    for j in range(m):
        if trash[i][j] == 1:
            dfs(i, j)
            area.append(len(count))
            count = []

if len(area):
    print(max(area))