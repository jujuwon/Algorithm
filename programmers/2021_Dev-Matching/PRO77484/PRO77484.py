def solution(lottos, win_nums):
    answer = []
    
    correct = 0
    zeroCount = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        elif lotto == 0:
            zeroCount += 1
            
    minLank = 6
    if correct > 0:
        minLank = 7 - correct
    
    maxCount = correct + zeroCount
    maxLank = 6
    if maxCount > 0:
        maxLank = 7 - maxCount
        
    answer.append(maxLank)
    answer.append(minLank)
    
    return answer