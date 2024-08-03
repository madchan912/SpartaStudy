# 유사 라임 게임 24431
import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
results = []

for _ in range(t):
    n, l, f = map(int, input().split())
    words = input().strip().split()

    # f 만큼 뒤에 자리수 자른 단어 리스트 생성
    sliced_words = [word[-f:] for word in words]

    # 카운터 함수로 해당 글자가 몇번 인지 확인
    counter = Counter(sliced_words)

    same_pair_count = 0

    # 각 글자가 2번 이상 나왔으면 나눈 몫을 결과에 저장
    for count in counter.values():
        same_pair_count += count // 2

    results.append(same_pair_count)

# 결과 출력
for result in results:
    print(result)