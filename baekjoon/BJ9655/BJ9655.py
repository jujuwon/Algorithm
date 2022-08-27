# baekjoon 돌 게임 (실버5)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
if N % 2 == 0:
    print('CY')
else:
    print('SK')