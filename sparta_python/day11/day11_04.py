# 단어 정렬 1181
import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
# 단어를 먼저 정렬하면서 중복 제거
words_asc = sorted(set(words))
words_dic = {}

# 딕셔너리에 글자와 글자수로 매칭
for i in range(len(words_asc)):
    words_dic[words_asc[i]] = len(words_asc[i])

# 딕셔너리에서 키값인 단어만 출력
words_dic_asc = sorted(words_dic.items(), key = lambda item:item[1])

for i in range(len(words_asc)):
    print(words_dic_asc[i][0])