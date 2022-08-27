# baekjoon 요세푸스 문제
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
print("<", end="")

for i in range(N - 1):
    for j in range(K - 1):
        queue.append(queue.popleft())
    print(f'{queue.popleft()}, ', end="")
print(f'{queue.popleft()}>')