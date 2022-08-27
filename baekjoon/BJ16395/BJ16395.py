# baekjoon 파스칼의 삼각형 (실버5)
import sys

def input():
    return sys.stdin.readline().rstrip()

pascal = [[1 for _ in range(30)] for _ in range(30)]

for i in range(2, 30):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    
n, k = map(int, input().split())
print(pascal[n-1][k-1])