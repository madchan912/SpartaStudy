# 3의 배수 1769
import sys
input = sys.stdin.readline

n = input().strip()

count = 0

while len(n) >= 2: # 두자리 숫자의 string의 len이 2
    y = 0
    for i in range(len(n)):
        y += int(n[i])
    n = str(y) # len을 구하기 위해 string으로 변경
    count += 1

print(count)
if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")