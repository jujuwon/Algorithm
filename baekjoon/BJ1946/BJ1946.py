# baekjoon 신입사원
import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for i in range(T):
    people = []
    cnt = 1

    N = int(input())
    for j in range(N):
        people.append(tuple(map(int, input().split())))
    
    people.sort()
    # 첫번째 사람은 서류 성적이 가장 좋으므로 무조건 합격
    # 첫번재 사람의 면접 점수를 기준으로 비교해서 합격 여부 결정하자
    max = people[0][1]

    for k in range(1, N):
        person = people[k][1]
        if person <= max:
            cnt += 1
            max = person
    print(cnt)
