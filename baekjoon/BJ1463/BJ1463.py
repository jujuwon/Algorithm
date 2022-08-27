# baekjoon 1로 만들기 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 일단 1을 빼는 연산을 진행한 값을 최소값으로 세팅
    dp[i] = dp[i - 1] + 1
    # 3으로 나누어 떨어지면 3으로 나누기
    if i % 3 == 0:
        # 1을 빼는 연산과, 3으로 나누는 연산을 비교해서 최소값으로 세팅
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        # 이전 연산과 2로 나누는 연산을 비교해서 최소값으로 세팅
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])