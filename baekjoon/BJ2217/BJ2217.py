# baekjoon 로프 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
rope = []

for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)

weight = 0

for i in range(N):
    temp = rope[i] * (i+1)
    if weight < temp:
        weight = temp

print(weight)