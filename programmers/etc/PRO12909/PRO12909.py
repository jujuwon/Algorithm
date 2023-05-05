# 올바른 괄호
'''
1. 스택을 하나 만든다.
2. loop 를 돌면서 여는 괄호가 들어오면 push, 닫는 괄호가 들어오면 pop
    - 만약 닫는 괄호가 들어왔는데, 스택이 비어있다면 false 리턴

만약 loop 가 끝났을 때 스택이 비어있다면 true 리턴, 아니면 false 리턴
'''
def solution(s):
    
    stack = []
    for ss in s:
        if ss == '(':
            stack.append(0)
        else:
            if not stack:
                return False
            stack.pop()
                
    if stack:
        return False
                
    return True