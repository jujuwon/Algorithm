# baekjoon 쇠막대기 문제
import sys

def input():
    return sys.stdin.readline().rstrip()

bracket = input()
stack = []
count = 0

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append("(")
    else:
        if bracket[i-1] == "(":
            # 레이저
            stack.pop()
            count += len(stack)
        else:
            # 막대 끝 위치일때
            stack.pop()
            count += 1

print(count)