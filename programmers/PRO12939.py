# 최댓값과 최솟값
def solution(s):
    numbers = list(map(int, s.split()))
    return str(min(numbers)) + ' ' + str(max(numbers))