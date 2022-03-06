# baekjoon 점프왕 쩰리 (Small)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 오른쪽과 아래만 갈 수 있음
dx = [0, 1]
dy = [1, 0]

def bfs(i, j):
    if not visited[i][j]:
        queue = deque([[i, j]])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            if x == (N-1) and y == (N-1):
                return True
            for k in range(2):
                xx = x + dx[k] * matrix[x][y]
                yy = y + dy[k] * matrix[x][y]
                if 0<=xx<N and 0<=yy<N:
                    if not visited[xx][yy]:
                        queue.append([xx, yy])
                        visited[xx][yy] = True
    return False

if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")