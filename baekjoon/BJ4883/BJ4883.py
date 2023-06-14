# baekjoon 삼각 그래프 (실버1)
import sys


def input():
    return sys.stdin.readline().rstrip()


k = 1

while True:
    N = int(input())

    if N == 0:
        break

    graph = [[] for _ in range(N)]

    for i in range(N):
        a, b, c = map(int, input().split())
        graph[i].append(a)
        graph[i].append(b)
        graph[i].append(c)

    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][0] = 1001
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]

    for i in range(1, N):
        dp[i][0] = graph[i][0] + min(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = graph[i][1] + min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
        dp[i][2] = graph[i][2] + min(dp[i][1], dp[i - 1][1], dp[i - 1][2])

    print(str(k) + ". " + str(dp[N - 1][1]))
    k += 1
