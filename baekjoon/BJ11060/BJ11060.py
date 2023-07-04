# baekjoon 점프 점프 (실버2)
import sys


def input():
    return sys.stdin.readline()


N = int(input())
jumps = list(map(int, input().split()))
dp = [-1 for _ in range(N)]
dp[0] = 0

for idx, jump in enumerate(jumps):
    if jump == 0 or dp[idx] == -1:
        continue
    for j in range(1, jump+1):
        if idx + j >= N:
            break
        if dp[idx + j] == -1 or dp[idx] + 1 < dp[idx + j]:
            dp[idx + j] = dp[idx] + 1

print(dp[N-1])
