# baekjoon ATM
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
P = sorted(list(map(int, input().split())))
time = 0

for i in range(1, N+1):
    for j in range(i):
        time += P[j]
        
print(time)