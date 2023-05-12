import sys
import heapq
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
gems = []

for _ in range(N):
    M, V = map(int, input().split())
    gems.append((M, V))
    
bags = []
for _ in range(K):
    bags.append(int(input()))
    
# 보석 무게 오름차순 정렬
gems.sort(key = lambda x : (x[0], -x[1]))
gems = deque(gems)
bags.sort()
result = 0
queue = []

for bag in bags:
    while gems and gems[0][0] <= bag: # 가방에 담을 수 있는 무게보다 커지면 break
        gem = gems.popleft()
        heapq.heappush(queue, -gem[1])
    if queue:
        result -= heapq.heappop(queue)
    
print(result)
