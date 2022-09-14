# programmers 문자열 압축 (Lv2 2020 KAKAO BLIND RECRUITMENT)
def solution(s):
    answer = len(s)
    
    # 압축 단위를 1부터 늘려가며 확인
    for i in range(1, len(s) // 2 + 1):
        str = ''
        tmp = s[:i]
        cnt = 1
        
        print("i: ", i)
        print("tmp: ", tmp)
        
        # 압축 단위만큼 증가시키며 이전 문자열과 비교
        for j in range(i, len(s), i):
            # 처음 자른 문자열과 동일하면 count 증가
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                # 숫자를 문자열에 더해주기
            
    
    return answer