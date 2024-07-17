#참외밭 2477 못품
import sys
input = sys.stdin.readline

k = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

big_w = 0
big_h = 0
big_w_index = 0
big_h_index = 0

# 큰 직사각형 두 변 구하기
for i in range(len(arr)):
  if arr[i][0] == 1 or arr[i][0] == 2 :
    if arr[i][1] > big_w:
      big_w = arr[i][1]
      big_w_index = i
  else:
    if arr[i][1] > big_h:
      big_h = arr[i][1]
      big_h_index = i

# 작은 직사각형 두 변 구하기
small_w = abs(arr[(big_h_index+1)%6][1] - arr[(big_h_index-1)%6][1])
small_h = abs(arr[(big_w_index+1)%6][1] - arr[(big_w_index-1)%6][1])

print((big_w*big_h - small_w*small_h) * k)