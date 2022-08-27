# baekjoon 토마토 (골드5)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def checkZero():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] == 0:
                    return True
    return False

def bfs():
    while queue:
        q = queue.popleft()
        x, y, z = q[0]
        for idx in range(6):
            xx = x + dx[idx]
            yy = y + dy[idx]
            zz = z + dz[idx]
            if 0 <= xx < H and 0 <= yy < N and 0 <= zz < M and matrix[xx][yy][zz] == 0:
                queue.append(((xx, yy, zz), q[1]+1))
                matrix[xx][yy][zz] = 1

    if checkZero():
        return -1
    else:
        return q[1]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, 0, 0, -1]
dz = [0, 0, 0, 1, -1, 0]
# x, y, z 세 방향 고려
# x -> H, y -> N, z -> M
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                queue.append(((i, j, k), 0))

print(bfs())