# 디펜스 게임
'''
- 종료조건 : 병사 수보다 적 수가 많으면 게임 종료.
- 라운드 진행 시마다 적 수만큼 병사 수 소모해야 이김
- 무적권 사용하면 라운드 승리
    - 무적권은 k 번 쓸 수 있음 -> 일단 k 번까지는 무조건 라운드 진행 가능하단 뜻!
- 무적권을 적절히 사용, 최대한 많은 라운드 -> 그리디 안됨
    최대한 많은 적이 있는 라운드에 무적권을 써야 함.

k+1 개 중에서 가장 적이 많은 k 개 라운드 뽑기. -> 무적권

if enemy길이 <= k:
    return enemy길이
    
heap에 k번째라운드까지 넣고시작 -> [2,4,4]
라운드=3
n=7

for -> N
    힙에 하나 넣기 -> logN
    하나 꺼내기 -> logN
    n 과 비교 이김? 라운드 += 1
    짐? return 라운드

return enemy길이

'''
import heapq

def solution(n, k, enemy):
    
    if len(enemy) <= k:
        return len(enemy)
    
    hq = []
    for idx in range(k):
        heapq.heappush(hq, enemy[idx])
    round = k
    
    for idx in range(k, len(enemy)):
        heapq.heappush(hq, enemy[idx])
        e = heapq.heappop(hq)
        if n < e:
            return round
        n -= e
        round += 1
        
    return len(enemy)