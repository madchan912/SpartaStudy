# 전주 듣고 노래 맞히기 31562
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
song = {}

# 글자수, 노래제목, 코드 7자리를 각각 확인 후 코드 3자리만 A 에 담아서 song 딕셔너리에 제목과 저장
for _ in range(n):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    A = [a1, a2, a3]	# 첫 세 음만 리스트로 저장
    song[S] = A		# key가 노래 제목, value가 첫 세 음

# 2중for문으로 코드랑 song안에 들어있는 노래 밸류랑 비교하여 출력
for _ in range(m):
    B = input().split()
    S = ''
    count = 0

    for s in song:
        if B == song[s]:
            count += 1
            S = s
    if count >= 2:
        print('?')
    elif count == 1:
        print(S)
    else:
        print('!')