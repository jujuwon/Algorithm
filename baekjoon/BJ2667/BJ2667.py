# baekjoon 단지번호붙이기 (실버1)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

matrix = [list(map(int, list(input()))) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
buildings = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            queue = deque([[i, j]])
            matrix[i][j] = 0
            count += 1
            building = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    xx = x+dx[k]
                    yy = y+dy[k]
                    if 0<=xx<N and 0<=yy<N and matrix[xx][yy] == 1:
                        building += 1
                        queue.append([xx, yy])
                        matrix[xx][yy] = 0
            buildings.append(building)
            
print(count)
for i in sorted(buildings):
    print(i)