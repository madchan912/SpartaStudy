# 별 찍기 - 19 10994
N = int(input())
# 공백 찍기
stars = [[' ' for _ in range(4 * N - 3)]  for _ in range(4 * N - 3)]

def draw_star(n, x, y):
    # 재귀에서 멈추는 역할(가운데)
    if n == 1:
        stars[y][x] = '*'
        return

    length = 4 * n - 3

    for i in range(length):
        stars[y][x + i] = '*' # 상단 * 출력
        stars[y + i][x] = '*' # 좌측 * 출력
        stars[y + length - 1][x + i] = '*' # 하단 * 출력
        stars[y + i][x + length - 1] = '*' # 우측 * 출력
    # 다음 사각형은 가로 세로 각 2칸씩 떨어져있음
    draw_star(n-1,x+2,y+2)

draw_star(N, 0, 0)

for s in stars:
    print(''.join(s))