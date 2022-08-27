# baekjoon 미로 탐색 (실버1)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]

cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque([[0, 0, 1]])
matrix[0][0] = 0
while queue:
    x, y, cnt = queue.popleft()
    if x == (N-1) and y == (M-1):
        break

    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        # 이동조건
        if 0<=xx<N and 0<=yy<M and matrix[xx][yy] != 0:
            queue.append([xx, yy, cnt + 1])
            matrix[xx][yy] = 0

print(cnt)