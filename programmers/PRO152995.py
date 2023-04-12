# 인사고과
'''
[근무태도점수, 동료평가점수]
- 딴 사람보다 한번이라도 둘다 낮으면, 인센 X
- 두 점수 합 높은 순으로 인센 차등 지급
    - 동일한 동석이면, 다음 석차 건너 뜀
    
NlogN 십만*17 => 17만
'''
def solution(scores):
    answer = 1
    
    me = scores[0]
    scores.sort(key=lambda x : (-x[0], x[1]))
    check = 0
    
    for score in scores:
        if me == score:
            if me[1] < check:
                return -1
            else:
                check = score[1]
                continue
        if score[1] >= check:
            check = score[1]
            if (score[0] + score[1]) > (me[0] + me[1]):
                answer += 1
    
    return answer