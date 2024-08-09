# 퇴사
import sys
input = sys.stdin.readline

def max_day(day, tp, memo):
    if day >= len(tp):
        return 0

    # visited 역할
    if day in memo:
        return memo[day]

    no_work_today = max_day(day + 1, tp, memo)

    # 걸리는 일이 최대 일자를 넘어가면 else 처리
    if day + tp[day][0] <= len(tp):
        work_today = tp[day][1] + max_day(day + tp[day][0], tp, memo)
    else:
        work_today = 0

    max_today = max(no_work_today, work_today)

    memo[day] = max_today

    return max_today

n = int(input())
job = []
for _ in range(n):
    job.append(list(map(int, input().split())))
memo = {}

result = max_day(0, job, memo)
print(result)