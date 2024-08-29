# 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

# 종료 시간을 기준으로 정렬
# 해당 문제 예시는 이미 되어있긴 한데 아래 식을 성립시키기 위해선 필요
time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
# 종료 시간 기준으로 정렬을 했기 때문에
# 가장 먼저 끝나는 회의를 최초 end_time으로 설정
end_time = time[0][1]

for i in range(1, n):
    # 시작 시간이 기존 끝 시간 보다 작거나 같으면 진행
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
