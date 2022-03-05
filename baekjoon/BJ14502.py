# baekjoon 연구소 (골드5)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

min_virus = 0

def bfs():
    # virus count
    cnt = 0
    queue = deque([])
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                queue.append([i, j])
                visited[i][j] = True
                cnt += 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        xx = x+dx[k]
                        yy = y+dy[k]
                        if 0<=xx<N and 0<=yy<M and matrix[xx][yy] == 0:
                            queue.append([xx, yy])
                            visited[xx][yy] = True
                            cnt += 1
    return cnt


def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    # 3개의 좌표를 선택해 벽을 세운 후 bfs 로 탐색
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                makewall(cnt + 1)
                matrix[i][j] = 0
                

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

'''
    0,0 부터 N-1, M-1 까지 벽을 세개 세운 후 bfs 로 바이러스 개수 확인
    그 중 가장 안전영역이 넓을 때를 선택
    안전영역의 넓이 출력
'''
ans = 0
makewall(0)
print(ans)