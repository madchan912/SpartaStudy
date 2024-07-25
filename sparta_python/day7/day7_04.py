# 큐 10845
import sys
input = sys.stdin.readline

# 각 명령어에 해당되는 함수 미리만듬
def push(x):
    queue.append(x)
def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))
def size():
    print(len(queue))
def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

N = int(input())

queue = []

# 입력받은 문자 확인 해서 명령어대로 함수 호출
for _ in range(N):
    command = input().strip().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
    else:
        print(-1)