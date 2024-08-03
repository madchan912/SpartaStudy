# 스피카 21316


from collections import defaultdict
import sys

input = sys.stdin.readline

# 선분 입력 받음
edges = [tuple(map(int, input().strip().split())) for _ in range(12)]

# 차수 계산 라이브러리 초기값 (딕셔너리)
degree = defaultdict(int)

# 각 지점 차수 계산
for x, y in edges:
    degree[x] += 1
    degree[y] += 1


# 스피카 초기값
spica = None

for node in degree:
    # 스피카의 차수는 3이므로 차수가 3일때
    if degree[node] == 3:
        degree_sum = 0  # 차수 합 초기값
        for x, y in edges:
            # 현재 연결(x,y)에서 x가 현재 검사 중인 노드인 경우
            # ex)현재 노드와 연결된 노드의 차수를 더해서 6이 되어야 함
            # (1,2)에서 x가 1이므로 degree[2]를 더해줌
            if x == node:
                degree_sum += degree[y]
            elif y == node:
                degree_sum += degree[x]

        # 스피카 조건 확인
        if degree_sum == 6:
            spica = node
            break

print(spica)
