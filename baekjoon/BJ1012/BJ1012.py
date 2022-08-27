# baekjoon 유기농 배추 (실버2)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for t in range(T):
    count = 0
    N, M, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    for num in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                queue = deque([[i, j]])
                matrix[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        xx = x+dx[k]
                        yy = y+dy[k]
                        if 0<=xx<N and 0<=yy<M and matrix[xx][yy] == 1:
                            queue.append([xx, yy])
                            matrix[xx][yy] = 0
                count += 1
    print(count)
