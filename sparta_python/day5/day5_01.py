# 알고리즘 수업 - 알고리즘의 수행 시간 4 24265
import sys
input = sys.stdin.readline
n = int(input())

print(int(((n - 1) * n) / 2))
print(2)

'''
예제기준 바깥 for문에서 1 ~ 6까지 
안쪽 for문에서 1일때 2~7 6개
2일때 3~7 5개 ... 6일때 1개 해서 1~6까지의 합
((1 + n) * n) / 2 에서 n이 n-1 이므로
((n - 1) * n) / 2
'''