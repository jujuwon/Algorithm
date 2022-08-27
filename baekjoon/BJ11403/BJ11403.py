# baekjoon 경로 찾기 (실버1)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start):
    visited = [0] * (N)
    queue = deque([start])

    while queue:
        n = queue.popleft()
        for i, v in enumerate(graph[n]):
            if visited[i] == 0 and v == 1:
                queue.append(i)
                visited[i] = 1
    return visited

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    print(' '.join(map(str, bfs(i))))