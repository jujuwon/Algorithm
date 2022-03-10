# baekjoon 최단경로 (골드5)
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

INF = 1e9

V, E = map(int, input().split())
K = int(input())
# graph = defaultdict(list)
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist:
            continue

        for g in graph[cur]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                heapq.heappush(queue, (cost, g[0]))
                distance[g[0]] = cost

dijkstra(K)

for i in range(1, V+1):
    print("INF") if (distance[i] == INF) else print(distance[i])