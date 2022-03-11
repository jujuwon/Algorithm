# 이것이 코딩 테스트다 - 큰 수의 법칙 (CHAT3 그리디 예제문제)
'''
1. 가장 큰 수를 K 만큼 연속해서 더한다.
2. 인덱스는 다르지만 같은 수 or 그 다음으로 큰 수를 K 만큼 더한다.
'''
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution_first():
    # N : 배열의 크기, M : 더해지는 횟수, K : 최대 연속 덧셈 가능 횟수
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    first = nums[N-1]
    second = nums[N-2]

    ans = 0
    cnt = 0
    for i in range(M):
        # 최대값 더하기
        if cnt < K:
            ans += first
            cnt += 1
        # 그 다음으로 큰 값 더하기
        else:
            ans += second
            cnt = 0

    print(ans)

'''
위 코드를 개선해보자 !
M 의 크기가 커진다면 시간 초과 날 수 있음
반복되는 수열을 파악 !
'''
def solution_second():
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    first = nums[N-1]
    second = nums[N-2]

    # 가장 큰 수가 더해지는 횟수 계산
    count = int(M / (K+1)) * K
    count += M % (K+1)
    
    ans = first * count
    ans += second * (M - count)

    print(ans)


if __name__ == "__main__":
    # solution_first()
    solution_second()