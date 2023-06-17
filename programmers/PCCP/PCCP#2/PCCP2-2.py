from collections import deque


def solution(menu, order, k):
    answer = 0

    # 현재 가게에 있는 손님 큐
    queue = deque()
    time = 0
    idx = 0

    while queue or idx < len(order):
        if queue:
            cur = queue.popleft()
            time += menu[cur]
        else:
            time = idx * k + menu[order[idx]]
            idx += 1

        while idx < len(order) and idx < (time / k):
            queue.append(order[idx])
            idx += 1
        answer = max(answer, len(queue))

    return answer + 1