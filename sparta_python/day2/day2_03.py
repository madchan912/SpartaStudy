# 별찍기 - 8 2445
import sys
input = sys.stdin.readline

a = int(input())

# i가 5까지
for i in range(1, a+1):
    # 왼쪽부터 * 1개부터 증가 여백 8 부터 2개씩 감소 * 1개부터 증가
    print('*' * i + " " * 2 * (a - i) + "*" * i)
# j 가 4까지
for j in range(1, a):
    # 왼쪽부터 * 5개부터 감소 여백 0 부터 2개씩 증가 * 5개부터 감소
    print('*' * (a - j) + ' ' * 2 * j + '*' * (a - j))