# baekjoon 후위 표기식2
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
formula = input()
dic = {}
num = deque()
stack = []

for i in range(N):
    num.append(int(input()))

for i in formula:
    if i not in dic and i.isalpha():
        dic[i] = num.popleft()
        
for i in formula:
    if i.isalpha():
        stack.append(dic[i])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == "+":
            stack.append(a + b)
        elif i == "-":
            stack.append(a - b)
        elif i == "*":
            stack.append(a * b)
        else:
            stack.append(a / b)
            
print(f'{stack[0]:.2f}')