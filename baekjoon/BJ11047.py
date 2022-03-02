# baekjoon 동전 0 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

ans = 0
for i in reversed(range(N)):
    ans += K // coins[i]
    K %= coins[i]
    
print(ans)