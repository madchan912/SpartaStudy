# 인공지능 시계 2530
h,m,s = map(int, input().split())
x = int(input())

second = h * 3600 + m * 60 + x + s # 전부 초로 변경

h = second // 3600 # 전체 초에서 시간
m = (second % 3600) // 60 # 전체 초에서 시간을 뺀 나머지 분
s = second % 60 # 전체 초에서 남은 초

if h >= 24: # 24시간이 넘어갈 경우 처리
    h %= 24

print(h,m,s)