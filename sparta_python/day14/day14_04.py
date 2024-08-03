# 그림 1926
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 그림이 있으면 1
    count.append(1)
    paper[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < m and paper[ny][nx] == 1:
            dfs(ny, nx)

n, m = map(int, input().split())

paper = []
count = []
area = []


for _ in range(n):
    paper.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            dfs(i, j)
            area.append(len(count))
            count = []

print(len(area))
# max 함수를 이용해 가장 컷던 count 값을 찾아냄
if len(area):
    print(max(area))
else:
    print(0)