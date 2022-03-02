# baekjoon DFS 와 BFS (실버2)
import sys
from collections import defaultdict, deque

def input():
    return sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
dic = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# 정점 번호 작은 것 부터 순회
for i in dic.keys():
    dic[i].sort()

# DFS
visited = [False] * (N+1)
def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    print(x, end= ' ')
    for i in dic[x]:
        dfs(i)
dfs(V)
print('')

# BFS
visited = [False] * (N+1)
queue = deque([V])
visited[V] = True
while queue:
    x = queue.popleft()
    print(x, end=' ')
    for i in dic[x]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True