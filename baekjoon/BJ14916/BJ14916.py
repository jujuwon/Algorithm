# baekjoon 거스름돈 (실버5)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
if N < 5:
    if N % 2 == 0:
        ans = N // 2
    else:
        ans = -1
else:
    num = N % 5
    if num % 2 == 0:
        ans = N // 5 + num // 2
    else:
        ans = (N // 5) - 1 + ((num + 5) // 2)

print(ans)