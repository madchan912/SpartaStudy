# 두 수 비교하기 1330
A,B = map(int, input().split())
answer = ''
if -10000 <= A and B <= 100000: #제한 조건
    if A > B: #왼쪽이 더 크면
        answer = '>'
    elif A < B: #오른쪽이 더 크면
        answer = '<'
    else: #그외이므로 같을 때
        answer = '=='
print(answer)

# early return 참고
