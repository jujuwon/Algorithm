import sys
from math import inf


def input():
    return sys.stdin.readline().rstrip()


# def permutation(arr, n):
#     result = []
#     if n == 0:
#         return [[]]
#
#     for arr_idx, arr_item in enumerate(arr):
#         for p in permutation(arr[:arr_idx] + arr[arr_idx+1:], n-1):
#             result += [[arr_item] + p]
#     return result
#
# # 첫번째 풀이 (완탐)
# def solution1():
#     N = int(input())
#     cities = [x for x in range(N)]
#     W = []
#
#     for i in range(N):
#         W.append(list(map(int, input().split())))
#
#     min_val = inf
#     for idx, city in enumerate(cities):
#         for pmt in permutation(cities[:idx] + cities[idx + 1:], N - 1):
#             if W[city][pmt[0]] == 0 or W[pmt[-1]][city] == 0:
#                 continue
#
#             val = W[city][pmt[0]] + W[pmt[-1]][city]
#             flag = True
#
#             for p in range(len(pmt) - 1):
#                 dist = W[pmt[p]][pmt[p+1]]
#                 if dist == 0:
#                     flag = False
#                     break
#                 val += dist
#             if flag:
#                 min_val = min(min_val, val)
#     print(min_val)


def dfs(x, cost, depth):
    global min_val
    if depth == N:
        if W[x][first] > 0:
            min_val = min(min_val, cost + W[x][first])
        return

    for next in range(N):
        if W[x][next] > 0 and not visited[next]:
            visited[next] = True
            dfs(next, cost + W[x][next], depth + 1)
            visited[next] = False

# 두번째 풀이 (dfs + 백트래킹)
N = int(input())
cities = [x for x in range(N)]
W = []
min_val = inf

for i in range(N):
    W.append(list(map(int, input().split())))

visited = [False] * N
for n in range(N):
    first = n
    visited[n] = True
    dfs(n, 0, 1)
    visited[n] = False

print(min_val)
