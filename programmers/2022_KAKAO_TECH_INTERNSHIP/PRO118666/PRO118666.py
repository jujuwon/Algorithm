from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dic = defaultdict(int)

    for i in range(len(survey)):
        a = survey[i][:1]
        b = survey[i][1:]
        
        if choices[i] < 4:
            dic[a] += 4 - choices[i]
        if choices[i] > 4:
            dic[b] += choices[i] - 4
            
    # RT 중에 하나 고르기
    if dic['R'] < dic['T']:
        answer += 'T'
    else:
        answer += 'R'
    # CF 중에 하나 고르기
    if dic['C'] < dic['F']:
        answer += 'F'
    else:
        answer += 'C'
    # JM 중에 하나 고르기
    if dic['J'] < dic['M']:
        answer += 'M'
    else:
        answer += 'J'
    # AN 중에 하나 고르기
    if dic['A'] < dic['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer