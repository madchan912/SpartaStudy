# 좌표 압축 18870
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
X_asc = sorted(set(X))
dic = {}
# 순서대로 정렬 했기때문에 1번째꺼보다 작은 숫자의 갯수는 i 가 된다
for i in range(len(X_asc)):
    dic[X_asc[i]] = i

for i in X:
    print(dic[i], end=" ")