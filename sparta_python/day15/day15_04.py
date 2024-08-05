# 양 3184
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(y, x):
    global v_cnt, o_cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[y][x] = True
    # 해당 칸이 늑대면 추가 양이면 추가
    if field[y][x] == 'v':
        v_cnt += 1
    elif field[y][x] == 'o':
        o_cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < r and 0 <= nx < c and field[ny][nx] != '#' and not visited[ny][nx]:
            dfs(ny, nx)

r,c = map(int, input().split())
field = []
for _ in range(r):
    field.append(list(map(str, input().rstrip())))
visited = [[False] * c for _ in range(r)]
# dfs 속 늑대,양 마릿수
v_cnt = 0
o_cnt = 0
# 살아있는 늑대, 양 마릿수
live_v = 0
live_o = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            if field[i][j] != '#':
                dfs(i, j)
                if v_cnt < o_cnt:
                    live_o += o_cnt
                    # 다음 for 문을 위한 초기화
                    v_cnt = 0
                    o_cnt = 0
                else:
                    live_v += v_cnt
                    # 다음 for 문을 위한 초기화
                    v_cnt = 0
                    o_cnt = 0

print(live_o, live_v)