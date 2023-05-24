import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
children = list(map(int, input().split(' ')))

def solution1():
    idx = [0 for _ in range(N + 1)]

    for i, v in enumerate(children):
        idx[v] = i

    maxval = 0
    cnt = 1
    for num in range(1, N):
        if idx[num] < idx[num + 1]:
            cnt += 1
        else:
            maxval = max(maxval, cnt)
            cnt = 1

    print(N - maxval if N != 1 else 0)

def solution2():
    dp = [0 for _ in range(N+1)]
    for child in children:
        dp[child] = dp[child - 1] + 1

    print(N - max(dp) if N != 1 else 0)
