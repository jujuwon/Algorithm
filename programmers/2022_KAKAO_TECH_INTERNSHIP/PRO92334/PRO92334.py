# 신고 결과 받기
'''
{'신고된 유저' : ['신고한유저1', '신고한유저2', ...]}
'''
from collections import defaultdict

def solution(id_list, report, k):
    abuse = defaultdict(list)
    mail = defaultdict(int)
    
    for re in report:
        r = re.split()
        abuse[r[1]].append(r[0])
        
    for a in abuse.keys():
        abuse[a] = set(abuse[a])
        if len(abuse[a]) >= k:
            for caller in abuse[a]:
                mail[caller] += 1
    
    return [mail[id] for id in id_list]