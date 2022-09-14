# programmers 괄호 변환 (Lv2 2020 KAKAO BLIND RECRUITMENT)
       
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True
    
def solution(p):
    answer = ''
    
    # 빈 문자열
    if p == '':
        return answer
    
    # 문자열을 두 "균형잡힌 괄호 문자열" 로 분리
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    # 문자열 u가 올바른 괄호 문자열이라면 v 에 대해 1번부터 다시 수행
    if check_proper(u):
        answer = u + solution(v)
    # 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정 수행
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] += ')'
            else :
                u[i] += '('
        answer += "".join(u)
        
    return answer