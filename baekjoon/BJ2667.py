# baekjoon 단지번호붙이기 (실버1)
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
matrix = [list(input()) for _ in range(n)]
print(matrix)