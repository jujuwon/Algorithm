from collections import defaultdict

def solution(N, stages):
    answer = []
    
    count = defaultdict(int)
    mans = len(stages)
    fault = defaultdict(float)
    
    for stage in stages:
        count[stage] = count[stage] + 1
        
    for n in range(1, N+1):
        if mans == 0:
            fault[n] = 0
            continue
        fault[n] = count[n] / mans
        mans -= count[n]
        
    f_list = sorted(fault.items(), key=lambda x : (-x[1], x[0]))
    
    for f in f_list:
        answer.append(f[0])
    
    return answer