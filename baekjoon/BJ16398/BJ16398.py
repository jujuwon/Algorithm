# baekjoon 행성 연결 (골드 4)
import sys


def input():
    return sys.stdin.readline().rstrip()


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
edge = []

for i in range(1, N):
    for j in range(i):
        edge.append((matrix[i][j], i, j))
edge.sort()

answer = 0
for cost, i, j in edge:
    if find(i) != find(j):
        union(i, j)
        answer += cost

print(answer)
