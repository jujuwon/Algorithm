import math

def find(n, p):
    if n == 1:
        return 'Rr'
    
    parent = find(n-1, math.ceil(p / 4))
    if parent == 'RR' or parent == 'rr':
        return parent
    else:
        p %= 4
        if p == 1:
            return 'RR'
        elif p == 0:
            return 'rr'
        else:
            return 'Rr'
    

def solution(queries):
    answer = []
    
    for q in queries:
        answer.append(find(q[0], q[1]))
    
    return answer