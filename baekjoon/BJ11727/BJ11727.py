# baekjoon 2xn 타일링 2 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])