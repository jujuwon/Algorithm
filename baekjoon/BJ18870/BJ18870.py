#baekjoon 좌표 압축
'''
    set() 함수를 이용해 중복을 제거 !
    랭킹을 매기는 시스템이라고 생각해보자
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
nums2 = sorted(list(set(nums))) # 중복 제거 후, 오름차순 정렬한 리스트 생성

dic = {nums2[i]: i for i in range(len(nums2))}

for i in nums:
    print(dic[i], end=" ")