# baekjoon 계단 오르기 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
score = [int(input()) for _ in range(n)]

if n <= 3:
    print(sum(score))
else:
    # 3번째 칸까지 구해두기
    dp = [score[0], score[0] + score[1], max(score[0], score[1]) + score[2]]
    for i in range(3, n):
        maxVal = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])
        dp.append(maxVal)
    print(dp[-1])