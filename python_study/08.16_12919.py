# A와 B 2 못품
import sys
input = sys.stdin.readline

def dfs(t):
    if t == S:
        print(1)
        sys.exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])

S = list(input().strip())
T = list(input().strip())

dfs(T)

print(0)