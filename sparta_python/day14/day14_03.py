# 섬의 개수 4963
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y, x):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    field[y][x] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h and field[ny][nx] == 1:
            dfs(ny, nx)

while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0
    for _ in range(h):
        field.append(list(map(int, read().split())))
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)