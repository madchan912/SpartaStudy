# A/B -2 15792 18점
import sys
a, b = map(int, sys.stdin.readline().split())
#1000번째 자리까지 허용
print(f'{a/b:.1000f}')