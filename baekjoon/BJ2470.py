# baekjoon 두 용액
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
solution = list(map(int, input().split()))

solution.sort()
min = 2000000001
s1 = s2 = 1000000001
left, right = 0, N-1

while left != right:
    sum = solution[left] + solution[right]
    if abs(sum) < min: # min 에는 절대값이 가장 작은 수가 들어감
        s1 = solution[left]
        s2 = solution[right]
        min = abs(sum)
    if sum < 0:
        left += 1
    else:
        right -= 1

print(f'{s1} {s2}')