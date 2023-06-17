dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Point:
    def __init__(self, x, y, flag, cnt):
        self.x = x
        self.y = y
        self.flag = flag
        self.cnt = cnt


def solution(n, m, hole):
    answer = 0

    matrix = [[True] * m for _ in range(n)]

    # 함정 표시
    for h in hole:
        matrix[h[0] - 1][h[1] - 1] = False

    queue = []
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    queue.append(Point(0, 0, False, 0))
    visited[0][0][False] = True

    while queue:
        cur = queue.pop()
        for i in range(4):
            xx = cur.x + dx[i]
            yy = cur.y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy][cur.flag] and matrix[xx][yy]:
                if xx == n - 1 and yy == m - 1:
                    return cur.cnt
                queue.append(Point(xx, yy, cur.flag, cur.cnt + 1))
                visited[xx][yy][cur.flag] = True

            # 아직 신발 사용 안함
            if not cur.flag:
                xx += dx[i]
                yy += dy[i]

                if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy][True] and matrix[xx][yy]:
                    if xx == n - 1 and yy == m - 1:
                        return cur.cnt
                    queue.append(Point(xx, yy, True, cur.cnt + 1))
                    visited[xx][yy][True] = True

    return -1


if __name__ == '__main__':
    print(solution(4, 4, [[2, 3], [3, 3]]))
    # print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))

