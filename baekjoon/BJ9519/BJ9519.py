# baekjoon 졸려 (골드5)
import sys


def input():
    return sys.stdin.readline().rstrip()


def wink(word_list):
    if len(word_list) % 2 == 0:
        index = len(word_list) - 1
    else:
        index = len(word_list) - 2
    while index > 0:
        word_list.append(word_list.pop(index))
        index -= 2
    return word_list


X = int(input())
word = input()
answer = list(word)

count = 0
for _ in range(X):
    answer = wink(answer)
    count += 1
    if list(word) == answer:
        break

count = X % count
for _ in range(count):
    answer = wink(answer)

print(''.join(answer))
