# baekjoon 연결 요소의 개수 (실버2)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        V = queue.popleft()
        for v in graph[V]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)