# programmers 신고 결과 받기 (Lv1 2022 KAKAO BLIND RECRUITMENT)
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)

    who_report = defaultdict(list)
    num_of_reported = defaultdict(int)
    stops = []

    for r in report:
        do_report, be_reported = r.split()

        num_of_reported[be_reported] += 1
        who_report[do_report].append(be_reported)

        if k == num_of_reported[be_reported]:
            stops.append(be_reported)

    for stop in stops:
        for i in range(len(id_list)):
            if stop in who_report[id_list[i]]:
                answer[i] += 1

    return answer