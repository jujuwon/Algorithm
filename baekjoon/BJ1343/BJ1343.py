import sys

def input():
    return sys.stdin.readline().rstrip()

str = input()

str = str.replace("XXXX", "AAAA")
str = str.replace("XX", "BB")

if 'X' in str:
    print(-1)
else :
    print(str)