from collections import deque

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    origin_len = len(queue1)
    cnt = 0
    
    # 두 큐 원소들을 전부 더한 값이 홀수이면 answer = -1
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    # len(queue1)의 4배 만큼 돌렸는데도 안 되면 return -1
    while True:
        
        if cnt > origin_len * 4:
            return -1
        
        if sum1 > sum2:
            q1 = queue1.popleft()
            queue2.append(q1)
            sum1 -= q1
            sum2 += q1
        elif sum1 == sum2:
            return cnt
        else:
            q2 = queue2.popleft()
            queue1.append(q2)
            sum2 -= q2
            sum1 += q2
        cnt += 1
    
    return -1