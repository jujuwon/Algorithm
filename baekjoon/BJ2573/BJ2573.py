import sys


def input():
    return sys.stdin.readline().rstrip()


def bfs(x, y):
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop()

        # 0 개수만큼 줄이기
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M:
                if matrix[xx][yy] != 0 and not visited[xx][yy]:
                    queue.append((xx, yy))
                    visited[xx][yy] = True
                elif matrix[xx][yy] == 0:
                    cnt[x][y] += 1
    return True


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = []
for m in range(N):
    matrix.append(list(map(int, input().split())))

day = 0
flag = False

while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = [[0 for _ in range(M)] for _ in range(N)]
    bfs_cnt = 0
    flag = False
    for m in range(M):
        for n in range(N):
            if matrix[n][m] != 0 and not visited[n][m]:
                bfs_cnt += 1
                bfs(n, m)

    for m in range(M):
        for n in range(N):
            matrix[n][m] -= cnt[n][m]
            if matrix[n][m] < 0:
                matrix[n][m] = 0

    if bfs_cnt == 0:
        break
    elif bfs_cnt > 1:
        flag = True
        break
    day += 1

if flag:
    print(day)
else:
    print(0)
