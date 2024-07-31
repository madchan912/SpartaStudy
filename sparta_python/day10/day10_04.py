# 세준세비 1524
import sys
input = sys.stdin.readline

winner = ""

T = int(input())

for _ in range(T):
    # 빈칸빼기
    null = input()
    N, M = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    # 둘중 한명의 리스트가 0이 될때까지
    while len(s) != 0 and  len(b) != 0:
        if s[0] > b[0]:
            b.remove(b[0])
        elif s[0] < b[0]:
            s.remove(s[0])
        else:
            b.remove(b[0])


    if len(s) == 0:
        winner = "B"
    elif len(b) == 0:
        winner = "S"
    else:
        winner = "C"
    print(winner)