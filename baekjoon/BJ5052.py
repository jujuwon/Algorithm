# baekjoon 전화번호 목록 (골드4)
import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for i in range(t):
    n = int(input())
    nums = sorted(list(input() for _ in range(n)))

    flag = True
    for k in range(n-1):
        cur = nums[k]
        next = nums[k+1]
        # cur in next 썼다가 계속 틀림 ..
        # 시작하는 부분만 비교 !
        if next.startswith(cur):
            flag = False
            break

    if flag:
        print("YES") 
    else:
        print("NO")