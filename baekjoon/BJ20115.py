# baekjoon 에너지 드링크 (실버3)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

result = drinks[N-1]
for i in range(N-1):
    result += drinks[i] / 2
print(result)