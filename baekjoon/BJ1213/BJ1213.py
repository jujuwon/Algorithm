import sys

def input():
    return sys.stdin.readline().rstrip()

count = {}
answer = []
name = list(input())
for n in name:
    if count.get(n, 0) == 0:
        count[n] = 1
    else:
        count[n] += 1

keys = sorted(count.keys())

odd_flag = False
odd_char = ''

for key in keys:
    if count[key] % 2 != 0:
        if odd_flag:
            print("I'm Sorry Hansoo")
            exit(0)
        else:
            odd_flag = True
            odd_char = key

answer = ''
for key in keys:
    answer = answer + key * int(count[key] // 2)
appendix = answer[::-1]
if odd_flag:
    answer += odd_char
answer += appendix

print(answer)
