# baekjoon 듣보잡
'''
    전체 리스트 순회하면 시간초과 !
    set 으로 변환 후 & 연산이나, interaction 함수를 이용해 
    교집합을 찾자 !
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

hear_names = [input() for i in range(N)]
see_names = [input() for i in range(M)]

names = list(set(hear_names) & set(see_names))
names.sort()

print(len(names))
for name in names:
    print(name)