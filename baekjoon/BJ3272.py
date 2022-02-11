# baekjoon 두 수의 합
'''
    배열로 2중 for loop 돌았을 땐 시간 초과,
    포인터 두 개를 사용해 이분 탐색하는 느낌으로 가자
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
l = 0
r = N - 1
cnt = 0

while True:
    if r <= l:
        break
    sum = nums[l] + nums[r]
    if sum == x:
        cnt += 1
        l += 1
        r -= 1
    elif sum < x:
        l += 1
    else :
        r -= 1

print(cnt)