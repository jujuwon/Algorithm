# programmers 주차 요금 계산 (Lv2 2022 KAKAO BLIND RECRUITMENT)
import math

def timeToSec(time):
    a, b = time.split(":")
    return int(a)*60 + int(b)
    
def solution(fees, records):
    answer = []
    
    park = {}
    result = {}
    
    for record in records:
        time, carNum, history = record.split()

        if history == "IN" : #입차
            park[carNum] = time
            if carNum not in result.keys():
                result[carNum] = 0
        else : #출차
            # outTime = datetime.strptime(time, "%H:%M")
            # inTime = datetime.strptime(park.pop(carNum), "%H:%M")
            
            # result[carNum] += int((outTime - inTime).seconds / 60)
            result[carNum] += timeToSec(time) - timeToSec(park.pop(carNum))
    
    # 만약 주차장에 입차기록만 있고 출차가 없다면
    for carNum in park.keys():
        # outTime = datetime.strptime("23:59", "%H:%M")
        # inTime = datetime.strptime(park[carNum], "%H:%M")
        # result[carNum] += int((outTime - inTime).seconds / 60)
        result[carNum] += timeToSec("23:59") - timeToSec(park[carNum])
        
    # fees[1] + Math.올림((result) - fees[0]) / fees[2]) * fees[3]
    sorted_dict = sorted(result.items())
    for dict in sorted_dict:
        #print('carNum : ', dict[0], ' result time : ', dict[1])
        if dict[1] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((dict[1] - fees[0]) / fees[2]) * fees[3])
    
    return answer