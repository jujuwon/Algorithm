# baekjoon 특정 거리의 도시 찾기 (실버2)
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

INF = 1e9
# N: 도시의 개수, M: 도로의 개수, K: 거리 정보, X: 출발 도시의 번호
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist:
            continue

        for g in graph[cur]:
            # g[0]: node 번호, g[1]: 가중치
            cost = dist + g[1]
            if cost < distance[g[0]]:
                heapq.heappush(queue, (cost, g[0]))
                distance[g[0]] = cost

dijkstra(X)
ans = []
for i, d in enumerate(distance):
    if d == K:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for a in ans:
        print(a)