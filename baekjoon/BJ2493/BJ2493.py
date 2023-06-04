import sys


def input():
    return sys.stdin.readline()


N = int(input())
towers = list(map(int, input().split()))

stack = []
answer = []

'''
스택이 비면 0
수신탑 찾을 때까지 peek.
    나보다 작은 값은 뒤 탑들에겐 필요없으므로 pop
    수신탑 찾으면 해당탑의 idx + 1 출력
나 push
'''
for idx, tower in enumerate(towers):
    while stack:
        if stack[-1][0] < tower:
            stack.pop()
        else:
            answer.append(str(stack[-1][1]))
            break
    else:
        answer.append(str(0))
    stack.append((tower, idx+1))

print(' '.join(answer))