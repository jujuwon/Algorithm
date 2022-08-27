# baekjoon 보물 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
S = 0

for i in range(N):
    S += A[i] * B.pop(B.index(max(B)))

print(S)