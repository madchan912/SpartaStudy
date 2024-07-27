# 알고리즘 수업 - 알고리즘의 수행 시간 6 24267
import sys
input = sys.stdin.readline

n = int(input())

print(int(n * (n - 1) * (n - 2) / 6))
print(3)

'''
n이 7일때
첫번째 for문에서 1 ~ 5까지
첫번째 for문의 i가 1 일때 
두번째 for문의 j는 2 ~ 6
k는 3 ~ 7

순서대로 써보면 123, 124, 125, 126, 127, 234, 235 ... 567
결과가 중복되는 않는 1~7까지의 숫자 조합
nC3 의 공식 사용
'''