# 이것이 코딩 테스트다 - 1이 될 때까지 (CHAT3 그리디 예제문제)
import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
cnt = 0
while N > 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    cnt += 1
print(cnt)