import sys


def input():
    return sys.stdin.readline().rstrip()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(height):
    res = 0
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if matrix[x][y] > height and not visited[x][y]:
                # 여기서부터 bfs 시작
                queue = [(x, y)]
                visited[x][y] = True

                while queue:
                    cx, cy = queue.pop()
                    for idx in range(4):
                        xx = cx + dx[idx]
                        yy = cy + dy[idx]
                        if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and matrix[xx][yy] > height:
                            queue.append((xx, yy))
                            visited[xx][yy] = True
                res += 1
    return res


N = int(input())
matrix = [[] for _ in range(N)]

max_val = 0

for i in range(N):
    numbers = list(map(int, input().split()))
    for num in numbers:
        matrix[i].append(num)
        max_val = max(max_val, num)

result = 0
for i in range(max_val):
    # 최대 높이까지 돌면서 bfs 하기
    result = max(result, bfs(i))

print(result)
