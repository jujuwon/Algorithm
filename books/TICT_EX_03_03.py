# 이것이 코딩 테스트다 - 숫자 카드 게임 (CHAT3 그리디 예제문제)
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

result = 0
for _ in range(N):
    line = list(map(int, input().split()))
    min_value = min(line)
    result = max(result, min_value)
print(result)