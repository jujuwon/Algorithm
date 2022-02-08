# baekjoon 소트인사이드
import sys

def input():
    return sys.stdin.readline().rstrip()

N = input()
N = sorted(list(map(int, N)), reverse=True)

for i in N:
    print(i, end="")