# 부분수열의 합
import sys
input = sys.stdin.readline

def dfs(idx,sum):
    if idx == n:
       return
    sum += num[idx]
    visited[sum] = 1
    # 재귀로 수열의 모든 수의 합을 구함
    # 구하는 과정에서 새로운 sum이 나오면 visited 처리
    dfs(idx + 1, sum)
    # 구해진 총합에서 각각의 조합으로 빼면서 생기는 새로운 sum을 visited 처리
    dfs(idx + 1, sum - num[idx])

n = int(input())
num = list(map(int, input().split()))
max_sum = sum(num)
visited = [0] * (max_sum + 1)

dfs(0,0)
# 0번째 자리는 사용하지 않는 visited여서
# 1번째 자리부터 시작
# 최초로 0이 나오는 지점을 찾아서 실제 숫자를 찾기위해 +1
print(visited[1:].index(0) + 1)