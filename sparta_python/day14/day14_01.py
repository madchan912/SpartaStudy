# 헌내기는 친구가 필요해 21736
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    visited[x][y] = True
    # 사람을 만났을대 cnt + 1
    if graph[x][y] == 'P':
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 로 움직엿을때 벽이 아니면 재귀
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] != "X":
                dfs(nx,ny)

cnt = 0
n, m = map(int, input().split())
graph = list(input() for _ in range(n))
visited = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            dfs(i, j)
if cnt == 0:
    print("TT")
else:
    print(cnt)