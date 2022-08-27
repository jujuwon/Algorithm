# baekjoon 카드
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dic = {}

for i in range(N):
    num = int(input())
    if dic.get(num):
        dic[num] += 1
    else:
        dic[num] = 1

num = sorted(dic.items(), key=lambda x : (-x[1], x[0]))
print(num[0][0])

# dic = {num: 0 for num in nums}

# for i in nums:
#     dic[i] += 1

# num = 0
# cnt = 0

# for i in dic.keys():
#     if cnt < dic[i]:
#         num = i
#         cnt = dic[i]

# print(num)