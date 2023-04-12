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