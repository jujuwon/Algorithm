# baekjoon 일곱 난쟁이
'''
    7명을 합쳐서 100이라는 것은
    9명 중 2명을 제외한 합이 100이 된다는 말과 동일 !
    역으로 생각해보자.
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

h = [int(input()) for _ in range(9)]
total = sum(h)

for i in range(9):
    for j in range(i+1, 9):
        if 100 == total - (h[i] + h[j]):
            num1, num2 = h[i], h[j]
            h.remove(num1)
            h.remove(num2)
            
            h.sort()
            
            for k in range(len(h)):
                print(h[k])
            break
    if len(h) < 9:
        break