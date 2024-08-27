# 데스 나이트
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()
        for i in range(6):
            # 문제에서 주어진 6가지 방향 처리
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 이동 횟수 처리
                visited[nx][ny] = visited[x][y] + 1
                if nx == r2 and ny == c2:
                    return visited[nx][ny]
                queue.append((nx, ny))
    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * n for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

answer = bfs(r1, c1)
print(answer)