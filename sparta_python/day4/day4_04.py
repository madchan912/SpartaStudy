# 상수 2908
a,b = input().split()
# string 상태에서 역순으로 입력 후 int 로 변환
a = int(a[::-1])
b = int(b[::-1])

print(a if a > b else b)