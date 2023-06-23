# baekjoon 이모티콘 (골드4)
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def bfs(x, y):
    queue = deque([])
    visited = [[False for _ in range(S * 2 + 1)] for _ in range(S * 2 + 1)]
    queue.append((x, y, 0))

    while queue:
        x, y, cnt = queue.popleft()
        if x == S:
            return cnt
        # 복사 가능 (y = x)
        if not visited[x][x]:
            queue.append((x, x, cnt + 1))
            visited[x][x] = True
        # y 가 0 보다 크다면 붙여넣기 가능 (x += y)
        if y > 0 and x+y < S * 2 and not visited[x+y][y]:
            queue.append((x+y, y, cnt+1))
            visited[x+y][y] = True
        # 지우기 가능 (x -= 1)
        if not visited[x-1][y]:
            queue.append((x-1, y, cnt+1))
            visited[x-1][y] = True


S = int(input())
print(bfs(1, 0))