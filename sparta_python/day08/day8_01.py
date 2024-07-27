# 민균이의 비밀번호 9933
import sys
input = sys.stdin.readline

N = int(input())
password = []
reverse_password = []

for i in range(N):
    password.append(input().strip())
    reverse_password.append(password[i][::-1])

# 문자의 길이값을 기준으로 // 2 를 해서 중간위치를 찾아서 출력
# 중복 제거를 위해 break
for i in range(N):
    if password[i] in reverse_password:
        length = len(password[i])
        middle = length // 2
        print(length, end = " ")
        print(password[i][middle])
        break