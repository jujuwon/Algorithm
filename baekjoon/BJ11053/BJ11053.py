# baekjoon 가장 긴 증가하는 부분 수열 (실버2)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        # i 이전의 값이 i 보다 작으면 수열
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))