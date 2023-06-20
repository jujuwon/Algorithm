import sys
import re


def input():
    return sys.stdin.readline().rstrip()


# (100+1+ | 01)+
T = int(input())

answer = []

for _ in range(T):
    signal = input()
    comp = re.compile('(100+1+|01)+')
    flag = comp.fullmatch(signal)
    if flag:
        answer.append("YES")
    else:
        answer.append("NO")

print('\n'.join(answer))