# baekjoon 피보나치 수 5 (브론즈2)
import sys

def input():
    return sys.stdin.readline().rstrip()

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

n = int(input())
print(fibo(n))