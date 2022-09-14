# programmers 괄호 변환 (Lv2 2020 KAKAO BLIND RECRUITMENT)
from collections import deque

def separate(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]
        
def check(str):
    stack = deque()
    for s in str:
        if s == "(":
            stack.append(s)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False
    return True


def solution(p):
    answer = ''
    
    # 빈 문자열
    if len(p) == 0:
        return p
    
    # 문자열을 두 "균형잡힌 괄호 문자열" 로 분리
    u, v = separate(p)
    
    # 문자열 u가 올바른 괄호 문자열이라면 v 에 대해 1번부터 다시 수행
    if check(u):
        answer += u
        answer += solution(v)
    # 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정 수행
    else:
        #  빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        #  문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        #  ')'를 다시 붙입니다. 
        #  u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        #  생성된 문자열을 반환합니다.
        answer += '('
        answer += solution(v)
        answer += ')'
        
        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else :
                answer += '('
        
    return answer