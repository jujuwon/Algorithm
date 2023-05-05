'''
탑승한 사람 무게 x 좌석 간의 거리 곱 => 같다면 시소 짝꿍
시소 짝꿍이 되려면?

반복문 한번만에 하고 싶음 -> 정렬을 하고 진행하면 되나?
앉을 수 있는 경우
2,2 (3,3 - 4,4) 1:1
2,3 (3,2) 1:1.5
3,4 (4,3) 1:
2,4 (4,2) 1:2

몸무게 하나 잡고 2,3,4 에 위치시켰을 때
각각 반대쪽 2,3,4 에 올 수 있는 몸무게들을 비교
    -> 탐색하려면 결국 N^2 이므로
        탐색 시간 줄이려면 Map 을 이용하자 !
1. 반복문 돌면서 dic = {몸무게: 사람 수} 형태로 map 구현
2. 반복문 돌기
   for key in dic
    - 1) 몸무게가 같은 경우
        dic[key] length 가 1이면 다음.
        dic[key] length (n) 가 2이상이면 n * (n-1) / 2
    - 2) 몸무게가 다른 경우
        positions = (2,3) (3,2) (3,4) (4,3) (2,4) (4,2)
        for posA, posB in positions:
            내 포지션이 A 일 때 B 에 올 수 있는 몸무게를 구하기
            반대무게 = posA * 내무게 / 반대무게
            expect = posA * dic[key] / posB
            # 있어야 하는 몸무게가 하나라도 있다면 내 무게 개수 * 반대 무게 개수
            if dic[expect] length > 1:
                answer += dic[key] * dic[expect]
'''
from collections import defaultdict

def solution(weights):
    answer = 0
    positions = [(2,3), (3,2), (3,4), (4,3), (2,4), (4,2)]
    dic = defaultdict(int)
    
    for weight in weights:
        dic[weight] += 1
        
    print(dic)
    for weight in weights:
        if dic[weight] > 1:
            answer += dic[weight] * (dic[weight] - 1) / 2
        for posA, posB in positions:
            expect = posA * weight / posB
            if dic[expect] > 0:
                answer += dic[weight] * dic[expect]
        dic[weight] = 0
    
    return answer

solution([100, 180, 360, 100, 270])