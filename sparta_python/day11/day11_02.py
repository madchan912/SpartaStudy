# 신입 사원 1946
import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    # 1이 1개라도 있으면 무조건 합격
    # 정렬한 이후 for 문을 돌릴예정이여서 index = 0 은 무조건 합격 이므로 count = 1 부터 시작
    count = 1
    top = 0
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    # 순서대로 정렬
    rank_asc = sorted(rank)

    for i in range(1, len(rank_asc)):
        # for 문에서 2번째부터 시작하며 1번과 비교하여 면접 순위가 더 낮으면 해당 지원자로 탑을 변경
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            count += 1

    print(count)