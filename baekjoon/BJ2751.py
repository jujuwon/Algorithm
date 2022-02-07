# baekjoon 수 정렬하기 2
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num.sort()

for i in range(N):
    print(num[i])