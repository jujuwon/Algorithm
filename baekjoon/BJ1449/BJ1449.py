# baekjoon 수리공 항승
'''
    생각보다 깔끔하게 코드 짜기가 어려웠다..
    방심하지 말고 다시 해보기
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

N, L = map(int, input().split())
pipe = sorted(list(map(int, input().split())))

cnt = 0
end = 0

for p in pipe:
    if end < p:
        cnt += 1
        end = p + L - 1

print(cnt)