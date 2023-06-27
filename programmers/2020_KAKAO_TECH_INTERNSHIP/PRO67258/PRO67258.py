def solution(gems):
    answer = [1, len(gems)]
    gem_dict = {gems[0]: 1}
    kind = set(gems)
    len_range = 1e9
    
    left, right = 0, 0
    while left <= right and right < len(gems) - 1:
        if len(kind) == len(gem_dict):
            if (right - left) < len_range:
                len_range = right - left
                answer = [left+1, right+1]
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1
        else:
            right += 1
            gem_dict[gems[right]] = gem_dict.get(gems[right], 0)
            gem_dict[gems[right]] += 1
    
    return answer