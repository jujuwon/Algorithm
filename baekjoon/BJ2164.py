# baekjoon 카드2 문제
from collections import deque
import sys

N = int(sys.stdin.readline())

q = deque(range(1, N+1))

while True:
    a = q.popleft()
    if not q:
        print(a)
        break
    b= q.popleft()
    q.append(b)