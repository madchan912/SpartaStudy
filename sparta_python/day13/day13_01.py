# 그녀를 찾아서 16502
import sys
input = sys.stdin.readline

# 행렬 곱셈 함수
def multiply_matrix_vector(matrix, vector):
    result = [0.0 for _ in range(len(vector))]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

# 행렬 제곱 함수
def multiply_matrix_matrix(matrix1, matrix2):
    size = len(matrix1)
    result = [[0.0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

t = int(input())
m = int(input())
edges = []
# 각 간선별 관계 리스트 생성
for _ in range(m):
    store = list(map(str,input().split()))
    src, dst, prob = store[0], store[1], float(store[2])
    edges.append((src,dst,prob))

store_indices = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
stores = ['A', 'B', 'C', 'D']
n = len(stores)

# 전이 행렬 초기화 (4x4)
transition_matrix = [[0.0 for _ in range(n)] for _ in range(n)]

# 전이 행렬 구축
for (src, dst, prob) in edges:
    i, j = store_indices[src], store_indices[dst]
    transition_matrix[j][i] = prob


init_state = [0.25, 0.25, 0.25, 0.25]

# 전이 행렬을 time_units 만큼 거듭 제곱
power_transition_matrix = transition_matrix
for _ in range(t - 1):
    power_transition_matrix = multiply_matrix_matrix(power_transition_matrix, transition_matrix)

# 시간의 경과에 따른 상태 변화 계산 (행렬 곱셈)
final_state = multiply_matrix_vector(power_transition_matrix, init_state)

# 결과 출력
for i, prob in enumerate(final_state):
    print(f"{100 * prob:.2f}")