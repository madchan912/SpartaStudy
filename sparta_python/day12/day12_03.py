# 점프왕 쩰리 (Small) 16173
import sys
input = sys.stdin.readline

def dfs(y, x):
    # 도착했으면 1로 출력
    visited[y][x] = 1

    # 도착 위치에 있는 숫자만큼 이동 해야 되므로
    dy = [0, graph[y][x]]
    dx = [graph[y][x], 0]

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < N and visited[ny][nx] == 0:
            dfs(ny, nx)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 하 우 로만 움직일수 있음
dy = (1, 0)
dx = (0 ,1)

start = (0, 0)
# 바닥 판과 사이즈가 같은 판 하나 생성
visited = [[0] * N for _ in range(N)]

dfs(0, 0)

if visited[N-1][N-1] == 1:
    print('HaruHaru')
else:
    print('Hing')