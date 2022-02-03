# baekjoon 최대 힙
import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []

for i in range(N):
    num = int(input())
    if num == 0:
        if heap:
            min = heapq.heappop(heap)[1]
            print(min)
        else:
            print(0)
    else:
        heapq.heappush(heap, (-num, num))
            