# baekjoon 스택 수열 문제
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = []
result = []

flag = True
cur = 1

for i in range(N):
    num = int(input())
    while cur <= num:
       stack.append(cur)
       result.append("+")
       cur += 1
       
    if num == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = False
        break
    
if flag:
    for i in result:
        print(i)        
    