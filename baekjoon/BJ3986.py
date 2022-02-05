# baekjoon 좋은 단어
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
count = 0

for i in range(N):
    word = input()
    stack = []
    
    for i in word:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        count += 1
        
print(count)