# baekjoon 숫자 카드 (실버4)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
n_list = sorted(list(map(int, input().split())))
M = int(input())
m_list = list(map(int, input().split()))

dic = {}
result = [0] * M

for n in n_list:
    dic[n] = 1

for i in range(M):
    if dic.get(m_list[i]):
        result[i] = dic[m_list[i]]

for r in result:
    print(r, end=" ")