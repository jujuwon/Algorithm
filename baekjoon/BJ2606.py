# baekjoon 바이러스 (실버3)
'''
    현재 인접 리스트를 이용해 BFS 로 구현
    dict 로 바꿔서 구현해보자 !
'''
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start):
    cnt = 0
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True
    return cnt

n = int(input())
k = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(k):
    t1, t2 = map(int, input().split())
    graph[t1].append(t2)
    graph[t2].append(t1)

print(bfs(1))