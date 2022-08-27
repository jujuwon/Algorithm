# baekjoon 조합 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

dp = [[1 for _ in range(101)] for _ in range(101)]

for i in range(2, 101):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

n, m = map(int, input().split())
print(dp[n][m])