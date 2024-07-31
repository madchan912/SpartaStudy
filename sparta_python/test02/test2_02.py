# 파일 합치기 3 13975
import sys,heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    book_price = list(map(int, input().split()))
    heapq.heapify(book_price)
    price = 0

    while len(book_price) > 1:
        temp = 0
        a = heapq.heappop(book_price)
        b = heapq.heappop(book_price)
        temp += a + b
        price += temp
        heapq.heappush(book_price, temp)

    print(price)