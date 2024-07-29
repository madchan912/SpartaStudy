# 서로 다른 부분 문자열의 개수 11478
import sys
input = sys.stdin.readline

S = input().strip()

total = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        total.add(S[i:j+1])

print(len(total))