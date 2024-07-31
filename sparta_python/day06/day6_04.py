# 인사성 밝은 곰곰이 25192
import sys
input = sys.stdin.readline

N = int(input())
nic = set()
cnt = 0

for i in range(N):
    user = input().strip()
    if user == 'ENTER':
        user_set = set()
    elif user not in user_set:
        user_set.add(user)
        cnt += 1

print(cnt)