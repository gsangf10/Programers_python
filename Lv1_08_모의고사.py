# 모의고사

def solution(answers):
    answer = []

    # 각 사람이 찍는 패턴
    patt1 = [1, 2, 3, 4, 5]
    patt2 = [2, 1, 2, 3, 2, 4, 2, 5]
    patt3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 총 문제의 개수까지 패턴 삽입
    mtp_num = len(answers) // len(patt1)
    patt1 *= mtp_num+1
    mtp_num = len(answers) // len(patt2)
    patt2 *= mtp_num+1
    mtp_num = len(answers) // len(patt3)
    patt3 *= mtp_num+1

    # 각 사람별 점수
    score = [0, 0, 0]

    # 정답 체크
    for i in range(len(answers)):
      if answers[i] == patt1[i]:
        score[0] += 1
      if answers[i] == patt2[i]:
        score[1] += 1
      if answers[i] == patt3[i]:
        score[2] += 1
    
    # 가장 높은 점수 받은 사람 판별
    if score[0] == score[1]:
      if score[0] == score[2]:
        answer += [1, 2, 3]
      elif score[0] > score[2]:
        answer += [1, 2]
      else:
        answer += [3]
    elif score[0] == score[2]:
      if score[0] > score[1]:
        answer += [1, 3]
      else:
        answer += [2]
    elif score[0] > score[1]:
      if score[0] == score[2]:
        answer += [1, 3]
      elif score[0] > score[2]:
        answer += [1]
      else:
        answer += [3]
    else:
      if score[1] == score[2]:
        answer += [2, 3]
      elif score[1] > score[2]:
        answer += [2]
      else:
        answer += [3]

    return answer

answers = [1,2,3,4,5]
solution(answers)
