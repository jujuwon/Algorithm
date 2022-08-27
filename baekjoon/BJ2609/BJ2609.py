# baekjoon 최대공약수와 최소공배수 (실버5)
import sys

def input():
    return sys.stdin.readline().rstrip()

def gcd(a, b):
    while b != 0:
        t = a % b
        a, b = b, t
    return abs(a)

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))