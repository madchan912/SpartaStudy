# Yangjojang of The Year 11557
import sys
input = sys.stdin.readline

school = []
alchol = []

T = int(input())

for _ in range(T):
    N = int(input())
    for j in range(N):
        s,l = input().split()
        school.append(s)
        alchol.append(int(l))
    # 학교 와 술의 index값은 서로 같으므로
    first = alchol.index(max(alchol))
    print(school[first])