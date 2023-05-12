import sys

def input():
    return sys.stdin.readline().rstrip()

line = input().split('-')
numbers = []
for l in line:
    tmp = map(int, l.split('+'))
    numbers.append(sum(tmp))

answer = numbers[0]
for idx in range(1, len(numbers)):
    answer -= numbers[idx]
print(answer)