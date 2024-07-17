#평균은 넘겠지 4344
import sys

a = int(sys.stdin.readline()) # 첫번째 값 입력

for i in range(a):
    grades = list(map(int, sys.stdin.readline().split())) # 점수의 갯수와 점수들을 리스트로 입력
    sum = 0
    num = 0
    for i in range(1, grades[0]+1): # 합계와 평균을 구하는 for문
        sum += grades[i]
    avg = sum / grades[0]
    for i in range(1, grades[0]+1): # 평균과 점수를 비교해서 평균보다 큰 점수의 갯수를 구하는 for문
        if avg < grades[i]:
            num+=1
    print(f'{num/grades[0]*100:.3f}%') # f-string으로 바로 출력
    # 평균 이상 점수의 숫자를 전체로 나누고 :.3f f는 소수점 표현, .3은 3자리까지 표기하겠다는 뜻

