# 예전 풀이
def timeToDay(day_string):
    # string 들어오면 시간으로 바꾸기
    # 2000.01.02 -> 일수
    y, M, d = map(int, day_string.split('.'))
    return (y * 12 * 28) + (M * 28) + d
    

def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    for term in terms:
        a, b = term.split()
        dic[a] = int(b)
        
    today = timeToDay(today)
    
    for idx in range(len(privacies)):
        day, term = privacies[idx].split()
        if timeToDay(day) + dic[term] * 28 <= today:
            answer.append(idx+1)
    
    return sorted(answer)

# 2023.06.28 풀이
def timeToDay(day):
    y, m, d = day.split('.')
    return int(y) * 12 * 28 + int(m) * 28 + int(d)
    

def solution(today, terms, privacies):
    answer = []
    term = {}
    today = timeToDay(today)
    
    for t in terms:
        x, y = t.split()
        term[x] = int(y)
    
    for idx, p in enumerate(privacies):
        start_day, kind = p.split()
        if timeToDay(start_day) + term[kind] * 28 <= today:
            answer.append(idx+1)
    
    return answer