# 크레인 인형뽑기 게임
'''
스택만들기
1. board 에서 moves 대로 움직이기
2. 움직인 위치 열에서 인형이 있는 가장 위 행의 인형 가져오기 -> 원래 위치는 0으로 변경
3. stack 최상단의 숫자와 비교
    -> 같다면 터트리기
        최상단 pop
    -> 다르다면 push
        
'''

def solution(board, moves):
    answer = 0
    
    stack = []
    N = len(board[0])
    
    for move in moves:
        for n in range(N):
            if board[n][move-1] == 0:
                continue
            else:
                toy = board[n][move-1]
                board[n][move-1] = 0
                if len(stack) == 0:
                    stack.append(toy)
                else:
                    if stack[len(stack)-1] == toy:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(toy)
                break
    
    return answer