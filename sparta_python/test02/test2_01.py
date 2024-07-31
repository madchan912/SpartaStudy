# 식당 입구 대기 줄 26042
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
max_length = 0
last_stdn = ""

for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == '1':
        dq.append(cmd[1])
    else:
        dq.popleft()

        now_length = len(dq)

        if now_length > max_length:
            max_length = now_length
            last_stdn = dq[-1] if dq else 0
        elif now_length == max_length and dq:
            last_stdn = min(last_stdn, dq[-1])

print(max_length, last_stdn)