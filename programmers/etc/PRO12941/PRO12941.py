# 최솟값 만들기
'''
A 배열의 최솟값과 B 배열의 최댓값을 곱해서 더해야 최소가 됨. 반대도 가능
A 를 오름차순 정렬, B 를 내림차순 정렬하기 -> 2 * NlogN
A 와 B 를 이중 for loop 로 탐색하기. 이중 for loop 이지만, 전체 탐색이 아님. -> N
O(N) = 2 * NlogN + N = 2 * 1000 * 10 + 1000 = 21,000
'''
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for idx in range(len(A)):
        answer += A[idx] * B[idx]
    
    return answer

# 개선 코드
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])