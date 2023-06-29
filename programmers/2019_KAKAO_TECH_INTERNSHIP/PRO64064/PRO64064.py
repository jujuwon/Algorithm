def check(regex, input_str):
    if len(regex) != len(input_str):
        return False
    for idx in range(len(regex)):
        if regex[idx] == '*':
            continue
        elif regex[idx] != input_str[idx]:
            return False        
    return True

def dfs(depth, banned_id, user_id, tmp):
    if depth == length:
        result.append(tmp)
        return
    
    for i, u in enumerate(user_id):
        if not visited[i] and check(banned_id[depth], u):
            visited[i] = True
            tmp.append(u)
            dfs(depth+1, banned_id, user_id, tmp[:])
            tmp.pop()
            visited[i] = False
    

def solution(user_id, banned_id):
    answer = 0
    global result, length, visited
    result = []
    length = len(banned_id)
    print(length)
    
    visited = [False for _ in range(len(user_id))]
    dfs(0, banned_id, user_id, [])
    
    answer = len(set(''.join(sorted(x)) for x in result))
    return answer