# 가르침
import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not visited[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False

n, k = map(int, input().split())

# 기본으로 주어진 anta, tica에서 5글자를 이미 사용
if k < 5:
    print(0)
    exit()
# 모든 알파벳을 읽을 줄 알면 전체 다 읽을 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(input().rstrip()) for _ in range(n)]
visited = [0] * 26

for alphabet in ('a','c','i','n','t'):
    # ord 는 유니코드값으로 변경하는 함수
    # a의 값을 빼서 a가 0번째에 오게 하고
    # visited에 방문 처리
    visited[ord(alphabet) - ord('a')] = 1

dfs(0, 0)
print(answer)