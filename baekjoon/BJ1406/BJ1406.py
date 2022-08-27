# baekjoon 에디터
'''
    커서 위치를 index 로 활용해서 list 로 풀면
    시간초과가 나는 문제 !
    커서를 index 로 생각하지 말고
    커서를 기준으로 두 개의 list 로 생각해서
    항상 O(1) 접근을 하도록 해서 풀자 !
'''
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

str1 = list(input())
str2 = deque([])
M = int(input())

for i in range(M):
    cmd = input()
    if cmd == "L":
        if str1:
            str2.appendleft(str1.pop())
    elif cmd == "D":
        if str2:
            str1.append(str2.popleft())
    elif cmd == "B":
        if str1:
            str1.pop()
    else:
        str1.append(cmd.split()[1])

str1.extend(str2)
print("".join(str1))