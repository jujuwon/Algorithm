# baekjoon 덱 문제
'''
    아래 코드처럼 문자열 자르는 연산보단
    if 문으로 분기 비교 하나하나 하는 것이 더 빠름 !
'''
from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
queue = deque([])

for i in range(N):
    cmd = sys.stdin.readline().rstrip().split("_")
    if cmd[0] == "push":
        cmd = cmd[1].split()
        if cmd[0] == "front":
            queue.appendleft(cmd[1])
        else:
            queue.append(cmd[1])
    elif cmd[0] == "pop":
        if queue:
            if cmd[1] == "front":
                print(queue.popleft())
            else:
                print(queue.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    