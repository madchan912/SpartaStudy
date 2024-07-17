# 검증수 2475
A = map(int, input().split())
x = 0 #제곱한 a를 받을 변수
for a in A:
    x += a ** 2 #기존 x의 값에 a의 제곱을 더함
print(x % 10) #for문이 끝난 x값을 10으로 나눈 나머지를 구함