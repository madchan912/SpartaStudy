# Best Grass 6186
import sys
input = sys.stdin.readline

# 예전 테스트때 오목과 유사
# 몇개의 덩어리의 풀뭉치가 있는지 확인하는 문제
def dfs(y, x):
    graph[y][x] = '.'

    for k in range(4):
        # 우 상 좌 하 순으로 움직이며 해당 위치에 # 이 있는지 확인 있으면 추가로 또 있는지 확인 하는 재귀 함수
        ny = y + dy[k]
        nx = x + dx[k]
        # 그래프 영역 안에 있는지 확인 하는 조건문
        if ny >= 0 and nx >= 0 and ny < R and nx < C:
            if graph[ny][nx] == '#':
                dfs(ny, nx)

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
count = 0
# 우 상 좌 하로 이동하기 위한 dy,dx
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 그래프를 돌면서 확인
for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            dfs(i, j)
            # 함수를 돌아서 나온 한 묶음당 1개로 취급해서 count에 + 1
            count += 1

print(count)