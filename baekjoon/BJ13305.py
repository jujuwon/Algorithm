# baekjoon 주유소 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dist = list(map(int, input().split()))
costs = list(map(int, input().split()))

minVal = costs[0]
ans = 0

for i in range(N-1):
    if minVal > costs[i]:
        minVal = costs[i]
    ans += minVal * dist[i]

print(ans)