# baekjoon 좌표 정렬하기 2
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = []

for i in range(N):
    nums.append(tuple(map(int, input().split())))

nums.sort(key=lambda x : (x[1], x[0]))

for i in nums:
    print(f'{i[0]} {i[1]}')