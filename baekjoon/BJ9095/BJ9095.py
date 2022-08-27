# baekjoon 1,2,3 더하기 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * 11
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(n):
    print(dp[int(input())])