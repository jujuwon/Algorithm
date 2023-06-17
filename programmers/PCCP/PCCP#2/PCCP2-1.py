import heapq


def solution(ability, number):
    queue = []
    for a in ability:
        heapq.heappush(queue, a)

    for _ in range(number):
        a = heapq.heappop(queue)
        b = heapq.heappop(queue)
        summary = a + b
        heapq.heappush(queue, summary)
        heapq.heappush(queue, summary)

    return sum(queue)