# [1차] 캐시
'''
도시 이름을 queue 에서 찾는다
- queue 에 도시가 없는 경우 queue 에 해당 도시를 넣는다. (캐시 미스이므로 실행시간 +5)
    - if queue 가 비어있거나 가득차지 않았다면 바로 append
    - if queue 가 비어 있다면 바로 append
    - else queue 가 가득찼다면 가장 앞에 있는 요소를 popleft 하고 append 한다.
- queue 에 도시가 있는 경우 해당 인덱스에서 빼서 가장 뒤에 append 한다 (캐시 hit 이므로 실행시간 +1)
'''
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    time = 0
    
    for city_str in cities:
        city = city_str.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            time += 5
            if cacheSize == 0:
                continue
            elif len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
    
    return time

'''
도시 100,000개
0 < cache < 30 사이즈의 캐시에서 도시를 찾음.
30 * 100,000
'''