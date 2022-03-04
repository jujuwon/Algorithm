# baekjoon 문서 검색 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

doc = input()
word = input()
ans = 0

while True:
    idx = doc.find(word)
    if idx == -1:
        break
    ans += 1
    doc = doc[idx + len(word):]

print(ans)