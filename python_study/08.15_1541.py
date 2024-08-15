# 잃어버린 괄호
import sys
input = sys.stdin.readline

def min_exp(a):
    # -를 기준으로 뒤의 값이 더 크면 최솟값
    parts = a.split('-')
    sums = []
    for part in parts:
        # 나눈걸 기준으로 + 해서 합을 구함
        numbers = list(map(int, part.split('+')))
        sums.append(sum(numbers))

    # 맨 앞의 값에서 뒤에 -로 나눠논 조합들의 합을 뺌
    result = sums[0]
    for s in sums[1:]:
        result -= s

    return result

a = input().strip()

min_value = min_exp(a)
print(min_value)