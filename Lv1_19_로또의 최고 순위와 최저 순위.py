# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []

    # 당첨 번호의 갯수
    correct_cnt = 0
    # 알아볼 수 없는 번호의 갯수
    unknown_cnt = lottos.count(0)

    # 최고 순위, 최저 순위
    max_prize = 0
    min_prize = 0
    
    # 당첨 번호 갯수 count
    for i in win_nums:
      if lottos.count(i) > 0:
        correct_cnt += 1
    
    # 알수 없는 번호와 당첨 확인된 번호를 비교하여 최고 순위 판별
    if unknown_cnt + correct_cnt == 6:
      max_prize = 1
    elif unknown_cnt + correct_cnt == 5:
      max_prize = 2
    elif unknown_cnt + correct_cnt == 4:
      max_prize = 3
    elif unknown_cnt + correct_cnt == 3:
      max_prize = 4
    elif unknown_cnt + correct_cnt == 2:
      max_prize = 5
    else:
      max_prize = 6

    # 당첨 확인된 번호를 비교하여 최저 순위 판별
    if correct_cnt == 6:
      min_prize = 1
    elif correct_cnt == 5:
      min_prize = 2
    elif correct_cnt == 4:
      min_prize = 3
    elif correct_cnt == 3:
      min_prize = 4
    elif correct_cnt == 2:
      min_prize = 5
    else:
      min_prize = 6
    
    # 확인된 최고 순위와 최저 순위를 정답 배열에 추가
    answer.append(max_prize)
    answer.append(min_prize)

    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

solution(lottos, win_nums)
