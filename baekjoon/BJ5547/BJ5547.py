# baekjoon 일루미네이션 (골드5)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

# y의 홀짝 여부에 따라 탐색할 인덱스가 달라짐

dx_odd = [-1, -1, 0, 1, 1, 0]
dy_odd = [0, 1, 1, 1, 0, -1]
dx_even = [-1, -1, 0, 1, 1, 0]
dy_even = [-1, 0, 1, 0, -1, -1]

W, H = map(int, input().split())
matrix = [[0 for _ in range(W+2)] for _ in range(H+2)]
for i in range(1, H+1):
    matrix[i][1:W+1] = map(int, input().split())

def bfs(x, y):
    queue = deque([])
    visited = [[False for _ in range(W+2)] for _ in range(H+2)]
    queue.append([x, y])
    visited[x][y] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()

        for i in range(6):
            xx, yy = 0, 0
            if x % 2 == 0:
                xx = x + dx_even[i]
                yy = y + dy_even[i]
            else:
                xx = x + dx_odd[i]
                yy = y + dy_odd[i]
            
            if 0 <= xx < H+2 and 0 <= yy < W+2:
                if matrix[xx][yy] == 0 and not visited[xx][yy]:
                    queue.append([xx, yy])
                    visited[xx][yy] = True
                elif matrix[xx][yy] == 1:
                    cnt += 1
    return cnt

print(bfs(0, 0))