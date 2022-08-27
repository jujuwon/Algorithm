# baekjoon 회의실 배정
'''
    회의 시작시간과 끝시간을 Tuple 로 저장하고 정렬
    - 빨리 끝나는 회의 순으로 먼저 정렬
    - 빨리 시작하는 회의 순으로 이후 정렬
    lambda 를 key 로 해서 다중 조건 정렬 가능
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
meeting = []
count = 1

for i in range(N):
    meeting.append(tuple(map(int, input().split())))
    
meeting.sort(key=lambda x : (x[1], x[0]))
end = meeting[0][1]

for i in range(1, N):
    if meeting[i][0] >= end:
        count += 1
        end = meeting[i][1]
        
print(count)