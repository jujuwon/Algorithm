# baekjoon 영화감독 숌 (실버5)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

i = 666
while N != 0:
    if '666' in str(i):
        N -= 1
        if N == 0:
            break
    i += 1

print(i)