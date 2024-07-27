# 문자열 반복 2675
a = int(input())

for _ in range(a):
    count, word = input().split()
    # 입력 받은 string c의 length만큼 for 문 돌리면서 b 갯수만큼 출력
    for i in range(len(word)):
        print(word[i] * int(count), end="")
    print()