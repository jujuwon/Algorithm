# 백준 거짓말 (골드4)
import sys


def input():
    return sys.stdin.readline()


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


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
truth = list(map(int, input().split()[1:]))
for t in truth:
    parent[t] = 0

parties = []
for m in range(M):
    tmp = list(map(int, input().split()))
    parties.append(tmp[1:])

    for p in range(len(parties[m]) - 1):
        union(parties[m][p], parties[m][p+1])

ans = 0
for m in range(M):
    flag = True
    for p in parties[m]:
        if parent[find(p)] == 0:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
