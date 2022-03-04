# programmers 소수 만들기 (Lv1 Summer/Winter Coding(~2018))
# 처음 풀이
def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                flag = True
                for n in range(2, int(num**0.5) + 1):
                    if num % n == 0:
                        flag = False
                if flag:
                    answer += 1
                        

    return answer

# 이후 풀이
def solution(nums):
    from itertools import combinations as cb
    
    answer = 0
    
    for i in cb(nums, 3):
        num = sum(i)
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                break
        else:
            answer += 1 

    return answer