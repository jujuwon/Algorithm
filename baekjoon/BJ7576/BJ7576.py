# baekjoon 토마토 (골드5)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])
            
def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            xx = x+dx[k]
            yy = y+dy[k]
            if 0<=xx<N and 0<=yy<M and matrix[xx][yy] == 0:
                matrix[xx][yy] = matrix[x][y] + 1
                queue.append([xx, yy])

bfs()
max = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        else:
            if max < j:
                max = j

print(max - 1)