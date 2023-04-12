# 이진 변환 반복하기
'''
while True:
    종료조건 - s가 "1" 이 될때
    1. 1의 개수 구하기
        기존 길이 = len(문자열)
        문자열s = 문자열s에서 0을 제거한것
        global 0의개수 += (기존길이 - len(문자열s))
    2. 1의 개수를 2진수로 변경
    global 변환횟수 += 1
'''
def solution(s):

    zeroCount = 0
    changeCount = 0

    while True:
        if s == "1":
            break
        length = len(s)
        s = s.replace("0", "")
        zeroCount += length - len(s)
        s = str(format(len(s), "b"))
        changeCount += 1        

    return [changeCount, zeroCount]

# 개선 코드
'''
어차피 1의 개수만 구하고, 이를 이진수로 변환하는 거니 replace 로 0을 지울 필요 없이
count('1') 로 개수만 구해주면 된다.
'''
def solution(s):

    zero, change = 0 ,0

    while s != '1':
        change += 1
        num = s.count('1')
        zero += len(s) - num
        s = format(num, "b")
        # s = bin(num)[2:]

    return [change, zero]