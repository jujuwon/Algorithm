# baekjoon 수 찾기 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

l = 0
r = trees[N-1]
ans = 0
maxVal = 0
flag = False

while l <= r:
    mid = (l+r) // 2
    temp = 0
    for tree in trees:
        if mid < tree:
            temp += (tree - mid)

    if temp == M:
        ans = mid
        flag = True
        break
    if temp < M:
        r = mid - 1
    else:
        maxVal = mid
        l = mid + 1

if flag:
    print(ans)
else:
    print(maxVal)