import sys


def input():
    return sys.stdin.readline().rstrip()


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    return int((a * b) / gcd(a, b))


a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

base = lcm(b1, b2)
top = (base // b1) * a1 + (base // b2) * a2
new_gcd = gcd(top, base)
base //= new_gcd
top //= new_gcd
print(f'{top} {base}')
