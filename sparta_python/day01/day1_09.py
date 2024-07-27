#설탕 배달 2839 while 문 이용
import sys

#설탕의 양
a = int(sys.stdin.readline())

#봉지의 갯수
x = 0
#설탕이 다 떨어질때까지
#만약 5의 배수면 바로 끝
#아닐경우 5의 배수가 될때까지 3씩 빼면서 봉지의 갯수를 늘림
# 0 보다 작은 값이 나오게 되면 else 로 -1 출력
while a >= 0:
    if a % 5 == 0:
        x += a // 5
        print(x)
        break
    a -= 3
    x += 1
else:
    print(-1)