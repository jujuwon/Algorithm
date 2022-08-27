# baekjoon 섬의 개수 (실버2)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                queue = deque([[i, j]])
                matrix[i][j] = 0
                cnt += 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<h and 0<=yy<w and matrix[xx][yy] == 1:
                            queue.append([xx, yy])
                            matrix[xx][yy] = 0
    print(cnt)
