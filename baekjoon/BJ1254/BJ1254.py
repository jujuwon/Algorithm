import sys

def input():
    return sys.stdin.readline().rstrip()

S = input()

answer = len(S)
for i in range(len(S)):
    tmp = S[i:]
    flag = True
    for j in range(len(tmp) // 2):
        if tmp[j] != tmp[len(tmp) - j - 1]:
            flag = False
            break
    if flag:
        answer += i
        break

print(answer)