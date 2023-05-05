def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * n
    for r in reserve:
        students[r-1] += 1
    for l in lost:
        students[l-1] -= 1
        
    for idx in range(len(students)):
        if students[idx] == 0:
            # 앞이나 뒤에서 가져오기
            if idx > 0 and students[idx-1] > 1:
                students[idx] += 1
                students[idx-1] -= 1
                continue
            elif idx < len(students) - 1 and students[idx+1] > 1:
                students[idx] += 1
                students[idx+1] -= 1
    
    answer = students.count(1)
    return answer