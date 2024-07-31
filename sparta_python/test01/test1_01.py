# 스위치 켜고 끄기 1244
import sys
input = sys.stdin.readline

def switch_control(num): # 호출되면 스위치 작동
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

n = int(input())
switch =list(map(int, input().split()))
s = int(input())

for _ in range(s):
    gender, num = map(int, input().split()) #순서대로 성별, 숫자카드
    if gender == 1: # 남자면
        for i in range(num-1, n, num): # 리스트가 0부터 시작이므로 num-1
            switch_control(i)
    else:
        switch_control(num-1) # 해당 숫자 먼저 끄고
        for j in range(n // 2):
            if num + j > n or num - j < 1: # 양끝에 닿으면 break
                break
            if switch[num-1 + j] == switch[num-1 - j]: # 기준 점에서 j만큼 떨어진 스위치가 같으면
                switch_control(num-1 + j)
                switch_control(num-1 - j)
            else:
                break
for i in range(0, n):
    print(switch[i], end=" ")
    if (i + 1) % 20 == 0: # 21번째 부터 다음줄로 넘겨야댐
        print()