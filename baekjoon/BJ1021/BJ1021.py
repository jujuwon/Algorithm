# baekjoon 회전하는 큐
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
want = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])
count = 0

for i in want:
    idx = queue.index(i)
    if idx == 0: # 첫번째면 그냥 pop
        queue.popleft()
    else:
        if idx <= len(queue) // 2: # 왼쪽으로 돌리는 게 유리
            queue.rotate(-idx)
            queue.popleft()
            count += idx
        else: # 오른쪽으로 돌리는 게 유리
            queue.rotate(len(queue) - idx)
            count += (len(queue) - idx)
            queue.popleft()

print(count)