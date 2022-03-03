# baekjoon 알바생 강호 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
q = [int(input()) for _ in range(N)]
q.sort(reverse=True)

ans = 0
for i in range(len(q)):
    tip = q[i] - ((i+1) - 1)
    if tip > 0:
        ans += tip

print(ans)