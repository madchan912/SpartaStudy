# 부등호
import sys
from itertools import permutations
input = sys.stdin.readline

def check_condition(perm, oper):
    for i in range(len(oper)):
        if oper[i] == '<' and perm[i] > perm[i+1]:
            return False
        if oper[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True

k = int(input())
oper = list(input().split())

# permutations는 순열로 모든 k + 1개를 사용한 순서쌍을 만듬
all_perms = permutations(range(10), k + 1)
valid_perms = []

# 모든 순서쌍에 대해 부등호 순서에 따라 맞는지 check_condition을 이용해서 확인
for perm in all_perms:
    if check_condition(perm, oper):
        valid_perms.append(''.join(map(str, perm)))

valid_perms.sort()
print(valid_perms[-1])
print(valid_perms[0])