# 영상처리 21938
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx]:
                if graph[ny][nx] == 255:
                    visited[ny][nx] = True
                    dfs(ny, nx)

n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for i in range(n)]
t = int(input())
#바꾼 픽셀 입력할 리스트
graph = [[] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    row = picture[i]
    for j in range(0, 3 * m, 3):
        avg = sum(row[j : j + 3])
        if t * 3 <= avg:
            avg = 255
        else:
            avg = 0
        graph[i].append(avg)

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if graph[i][j] == 255:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1

print(cnt)