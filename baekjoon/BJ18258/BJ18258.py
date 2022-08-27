'''
    10845 큐 문제와 동일한 문제
    최대 명령의 수가 10만에서 200만으로 달라짐.
    큐 문제를 풀 때 list 를 이용해서 queue 자료구조를 사용하면,
    pop(0) 같은 연산을 할 때 리스트 전체 데이터를 앞으로 한 칸씩 당겨줘야 하므로
    시간 복잡도는 O(N) 이 된다.
    queue 를 사용할 때는 collections 모듈의 deque 를 사용하자 !
'''
from collections import deque
import sys

N = int(sys.stdin.readline())

q = deque([])

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":    
        q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)