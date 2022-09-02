#baekjoon 피보나치 수 2 (브론즈1)
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

fibo = [0, 1]

for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])
    
print(fibo[n])