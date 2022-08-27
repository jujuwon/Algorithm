# baekjoon 균형잡힌 세상
import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    sen = input()
    stack = []
    
    if sen == '.':
        break
    
    for i in sen:
        if i == '(' or i =='[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if not stack:
        print('yes')
    else:
        print('no')