# baekjoon 다리 놓기 (실버5)
import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1

for num in range(1, 31):
    dp[num][0] = 1
    for pick in range(1, 31):
        if num == pick or pick == 0:
            dp[num][pick] = 1
        else:
            dp[num][pick] = dp[num-1][pick-1] + dp[num-1][pick]
            
for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M][N])