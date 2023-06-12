import sys


def input():
    return sys.stdin.readline().rstrip()


def sum_all(number):
    result = 0
    for x in number:
        if x.isdigit():
            result += int(x)
    return result

guitars = []

N = int(input())
for n in range(N):
    guitars.append(input())

guitars.sort(key=lambda x : (len(x), sum_all(x), x))

for guitar in guitars:
    print(guitar)
