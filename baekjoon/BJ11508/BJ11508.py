# baekjoon 2+1 세일 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
costs = [int(input()) for _ in range(N)]
costs.sort(reverse=True)
idx = 0
result = 0
for cost in costs:
    if idx == 2:
        idx = 0
        continue
    else:
        result += cost
        idx += 1

print(result)