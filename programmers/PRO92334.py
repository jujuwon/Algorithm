# programmers 신고 결과 받기 (Lv1 2022 KAKAO BLIND RECRUITMENT)
def solution(id_list, reports, k):
    answer = [0] * len(id_list)
    stops = []
    dic = {id: [] for id in id_list}
    
    for temp in set(reports):
        report = temp.split()
        stops.append(report[1])
        dic[report[1]].append(report[0])
    
    stops = set([i for i in stops if k <= stops.count(i)])
    print(f'stops : {stops}')
    print(dic)
    for stop in stops:
        for val in dic[stop]:
            answer[id_list.index(val)] += 1
            
    return answer