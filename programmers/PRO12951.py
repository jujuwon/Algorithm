# JadenCase 문자열 만들기
'''
    1. 반복문을 돌면서 str 을 한 인덱스씩 확인한다
    2. 조건을 체크하고 대문자 or 소문자로 변경한다
        2-1. 현재 인덱스의 문자가 '문자' 일 때
            - 문자열의 첫번째 문자라면 대문자로 변경한다
            - 이전 문자가 공백이라면 대문자로 변경한다
        그외 전부 소문자로 변경
'''
def solution(s):
    answer = ''
    
    jaden = []
    for idx in range(len(s)):
        if idx == 0 and s[idx].isalpha():
            jaden.append(s[idx].upper())
        elif s[idx-1] == ' ' and s[idx].isalpha():
            jaden.append(s[idx].upper())
        else:
            jaden.append(s[idx].lower())

    return ''.join(jaden)