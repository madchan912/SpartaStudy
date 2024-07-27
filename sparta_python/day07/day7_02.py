# 단어순서 뒤집기 12605
import sys
input = sys.stdin.readline

N = int(input())

words = [input().strip() for i in range(N)]

revers_words = []

for i in range(N) :
    revers_words = words[i].split(" ")
    print(f"Case #{i+1}: ", end="")
    for j in range(len(revers_words)):
        print(revers_words[-(j+1)], end=" ")
    print()

'''
기존 단어를 words에 받아서 reversed로 뒤집어서 출력
'''