# 주차 요금 계산

import math

def solution(fees, records):
    pk_info = {}
    car_time = {}
    for s in records:
      car_info = s.split()
      # 입차 기록이면 딕셔너리에 해당 차량번호와 입차 시간 기록
      if car_info[2] == 'IN':
        pk_info[car_info[1]] = car_info[0]
        # 해당 차량의 이전 이용 기록이 존재하지 않으면 신규 추가
        if car_info[1] not in car_time:
          car_time[car_info[1]] = 0
      # 출차 기록이면 요금 계산 후 해당 딕셔너리 삭제
      else:
        in_time = list(map(int,pk_info[car_info[1]].split(':')))
        out_time = list(map(int,car_info[0].split(':')))

        # 주차 시간 계산
        pk_hour = out_time[0] - in_time[0]
        pk_minute = out_time[1] - in_time[1]
        pk_time = (pk_hour*60) + pk_minute

        # 해당 차량의 하루 이용 시간 계산
        car_time[car_info[1]] += pk_time

        # 입차 기록 삭제
        del pk_info[car_info[1]]
    
    # 하루가 지나면 23:59분으로 출차 계산
    if len(pk_info) != 0:
      for k, v in pk_info.items():
        in_time = list(map(int,v.split(':')))

        # 주차 시간 계산
        pk_hour = 23-in_time[0]
        pk_minute = 59-in_time[1]
        pk_time = (pk_hour*60) + pk_minute

        # 해당 차량의 하루 이용 시간 계산
        car_time[k] += pk_time

    # 차량번호 순으로 정렬
    car_time = dict(sorted(car_time.items()))
    
    # 주차 요금 계산
    amt = []
    for v in car_time.values():
      # 기본시간일 경우 기본 요금
      if v <= fees[0]:
        amt += [fees[1]]
      # 기본시간을 초과한 경우 초과요금 부과
      else:
        amt += [fees[1] + (math.ceil((v-fees[0])/fees[2])*fees[3])]
        
    return amt

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)
