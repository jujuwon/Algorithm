# baekjoon 효율적인 해킹 (실버1)
'''
    python3 로는 계속 시간초과..
    PyPy3 로는 성공했다.
    파이썬으로 시간초과 안 나는 법을 찾아보자 ..!
'''
import sys
from collections import defaultdict, deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start):
    cnt = 1
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in com[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                cnt += 1
    return cnt

N, M = map(int, input().split())
com = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    com[b].append(a)

results = []
maxVal = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if maxVal < cnt:
        maxVal = cnt
    results.append([i, cnt])

for i, cnt in results:
    if cnt == maxVal:
        print(i, end=' ')