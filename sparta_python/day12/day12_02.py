# 바닥 장식 1388
import sys
input = sys.stdin.readline

# 가로 장식 함수
def dfs_w(y, x):
    graph[y][x] = '.'

    # 가로가 같은 지로만 확인 하면 되기 때문에 x + 1 만 함
    nx = x + 1
    if nx >= 0 and nx < M:
        if graph[y][nx] == '-':
            dfs_w(y,nx)

# 세로 장식 함수
def dfs_l(y, x):
    graph[y][x] = '.'

    ny = y + 1
    if ny >= 0 and ny < N:
        if graph[ny][x] == '|':
            dfs_l(ny, x)

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == '-':
            dfs_w(i, j)
            count += 1

        elif graph[i][j] == '|':
            dfs_l(i, j)
            count += 1

print(count)