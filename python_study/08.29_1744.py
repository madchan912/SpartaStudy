# 수 묶기
n = int(input())
numbers = sorted([int(input()) for _ in range(n)])

# 양수 음수 나누고 1은 바로 더해버리고
positive = []
negative = []
total = 0

for num in numbers:
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    else:
        total += 1

# 양수 처리: 큰 값끼리 곱하기
while len(positive) > 1:
    total += positive.pop() * positive.pop()

if positive:
    total += positive.pop()

# 음수 처리: 작은 값끼리 곱하기
while len(negative) > 1:
    total += negative.pop(0) * negative.pop(0)

# 음수가 남고 0이 있다면 0을 곱해서 처리
if negative:
    total += negative.pop()

print(total)
