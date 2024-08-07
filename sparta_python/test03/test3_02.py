# 구호물자 11581
import sys
input = sys.stdin.readline

n = int(input())
m = 0
visited = [[0] * n for _ in range(n)]

# 노드관계 표현
for i in range(n-1):
    m = int(input())
    node = map(int, input().split())
    for j in node:
        visited[i][j-1] = 1

# if visited[i][k] == 1 and visited[k][j] == 1: 는 서로 왓다갓다 할수 있다
for k in range(n):
    for i in range(n):
        for j in range(n):
            if visited[i][k] == 1 and visited[k][j] == 1:
                visited[i][j] = 1

answer = ''
for i in range(n):
    if visited[i][i] == 1 and visited[0][i] == 1:
        answer = 'CYCLE'
        break
    else:
        answer = 'NO CYCLE'
print(answer)