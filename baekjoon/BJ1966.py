# baekjoon 프린터 큐
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

case_count = int(input())

for i in range(case_count):
    doc_count, index = map(int, input().split())
    queue = deque(map(int, input().split()))
    count = 0
    
    while queue:
        best = max(queue) # 최댓값 저장
        front = queue.popleft() # 큐의 첫번째 pop
        index -= 1 # pop 했으므로 인덱스가 하나 줄어듬
        
        if best == front: # 뽑은 문서가 중요도 최대 -> 출력
            count += 1
            if index < 0: # 원하는 index 문서 출력
                print(count)
                break
        
        else: # 뽑은 문서가 중요도 최대가 아님 -> 제일 뒤로 보내기
            queue.append(front)
            if index < 0: # 원하는 index 문서가 뽑히면 index 를 제일 뒤로 이동
                index = len(queue) - 1