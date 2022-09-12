# programmers k진수에서 소수 개수 구하기 (Lv2 2022 KAKAO BLIND RECRUITMENT)
import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def solution(n, k):
    
    temp = ''
    while n:
        temp = str(n % k) + temp
        n //= k
    lst = temp.split('0')
    
    count = 0
    for l in lst:
        if l == '' or int(l) == 1:
            continue
        # 하나씩 소수인지 판별
        flag = True
        num = int(l)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
        if flag:
            count += 1
    
    return count
