# 구구단 2739
import sys
input = sys.stdin.readline

a = int(input())

for i in range(9):
    # f-string 으로 입력받은 값과 곱을 구하여 출력
    print(f'{a} * {i+1} = {a * (i+1)}')