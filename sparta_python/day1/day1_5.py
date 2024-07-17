# 주사위 세개 2480
a,b,c = map(int, input().split())
x = 0

if a == b == c:
    x = 10000 + (a * 1000)
elif a == b or b == c:
    x = 1000 + (b * 100)
elif a == c:
    x = 1000 + (a * 100)
else:
    x = max(a,b,c)*100

print(x)