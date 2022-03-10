# baekjoon 소수&팰린드롬 (실버1)
import sys

def input():
    return sys.stdin.readline().rstrip()

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())

result = 1003001
for i in range(N, 1000001):
    if str(i) == str(i)[::-1]:
        if isPrime(i):
            result = i
            break

print(result)