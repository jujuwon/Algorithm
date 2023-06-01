def solution(input_string):
    answer = []
    dic = {}

    for idx, ch in enumerate(input_string):

        if dic.get(ch, 0) == 0:
            dic[ch] = 1
        else:
            dic[ch] += 1
            if dic[ch] > 1 and idx > 1 and ch != input_string[idx -1]:
                answer.append(ch)

    if not answer:
        return 'N'

    answer = list(set(answer))
    answer.sort()
    return ''.join(answer)