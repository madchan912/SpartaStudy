# 콘서트 16466
import sys
input = sys.stdin.readline

# 계수정렬 활용
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        # 0번째에 1을 넣기 위해 -1
        count[num - 1] += 1

    # count 함수에 최대값 + 1개 만큼 만들고
    for i, c in enumerate(count):
        # 순서대로 돌면서 처음으로 0 인 인덱스가 나오는것 찾아서 +1
        if c == 0:
            return i + 1
            break

min_t = 0
N = int(input())
a = list(map(int, input().split()))

min_t = counting_sort(a)
print(min_t)