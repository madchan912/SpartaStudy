# 일곱 난쟁이 2309
import sys
input = sys.stdin.readline
error_1 = 0
error_2 = 0
result = []

# 퀵정렬 함수 / 피벗
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

short = [int(input()) for _ in range(9)]

# 난쟁이 키의 총합
sum_short = sum(short)

for i in range(8):
    for j in range(i+1, 9):
        # 2중포문으로 순서대로 매칭해서 2명을 뺏을때 100이 되면
        if sum_short - (short[i] + short[j]) == 100:
            error_1 = short[i]
            error_2 = short[j]

short.remove(error_1)
short.remove(error_2)
result = quick_sort(short)

for i in result:
    print(i)