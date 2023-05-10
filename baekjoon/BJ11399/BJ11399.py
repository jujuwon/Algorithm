# baekjoon ATM
import sys

def input():
    return sys.stdin.readline().rstrip()

# 첫번째 풀이
def solution_1():
    N = int(input())
    P = sorted(list(map(int, input().split())))
    time = 0

    for i in range(1, N+1):
        for j in range(i):
            time += P[j]
            
    print(time)
    
# 두번째 풀이
def solution_2():
    N = int(input())
    P = sorted(list(map(int, input().split())))
    sum = [0 for _ in range(N)]
    sum[0] = P[0]
    time = sum[0]
    
    for i in range(1, N):
        sum[i] = sum[i-1] + P[i]
        time += sum[i]
    print(time)
