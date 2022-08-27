# baekjoon 동전 1 (골드5)
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        if i-coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])