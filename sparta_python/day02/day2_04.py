# 뜨거운 붕어빵 11945
import sys
input = sys.stdin.readline

# 첫줄 출력
n, m = map(int, input().split())

for _ in range(n) :
    # 각 줄을 string 으로 list에 담고 reverse 함수로 뒤집음
    x = list(map(str, input().strip()))
    x.reverse()

    # 현재 상태로 출력하면 리스트 형태 이므로 1개 씩 출력
    # print 안의 end ='' 는 줄 바꿈 하지 않음
    for i in range(m) :
        print(x[i], end='')
        
    # 한줄 출력 완료 될때마다 줄 바꿈
    print()