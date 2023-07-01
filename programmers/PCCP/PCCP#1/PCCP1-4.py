import heapq

def solution(program):
    answer = [0 for _ in range(11)]
    # 프로그램을 호출시각으로 정렬
    program.sort(key = lambda x : -x[1])
    heap = []
    
    # 반복문 돌면서 while program or heap:
        
        # 리스트에서 현재시각보다 호출시각이 작거나 같은 애들을 heapq 에 rank 기준으로 넣기
        # if heapq:
            # pro = heappop
            # answer[pro.rank] += (cur - pro.calltime)
            # cur += pro.runtime
        # else:
            # 아직 시작할 게 없는 거임.
            # 현재 시각을 바꿔줘야 함.
            # cur = program.get(0)[1]
            
    while program or heap:
        while True:
            if program and program[-1][1] <= answer[0]:
                p = program.pop()
                heapq.heappush(heap, p)
            else:
                break
        
        if heap:
            pro = heapq.heappop(heap)
            answer[pro[0]] += (answer[0] - pro[1])
            answer[0] += pro[2]
        else:
            answer[0] = program[-1][1]
        
    return answer