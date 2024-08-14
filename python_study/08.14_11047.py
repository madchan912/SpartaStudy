# 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

amounts = []
for _ in range(n):
    amounts.append(int(input()))

count = 0
# 큰 금액부터 넣어서 잔액 출력하는 방식
for amount in reversed(amounts):
    if k >= amount:
        # 큰금액 넣고 나눳을때 몫이 사용된 갯수
        count += k // amount
        # 나머지가 새로운 목표 k로 변경
        k %= amount

print(count)