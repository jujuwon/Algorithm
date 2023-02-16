# baekjoon A+B-4 (브론즈5)
import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break