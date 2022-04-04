# 실패율

def solution(N, stages):
    answer = []
    f_rate = []

    # 각 스테이지 마다 실패율 계산
    for n in range(1,N+1):
      c_num = 0  # 해당 스테이지를 클리어한 플레이어 수
      s_num = 0  # 해당 스테이지에 멈춰있는 플레이어 수
      for p in stages:
        if p >= n:
          c_num += 1
        if p == n:
          s_num += 1
      
      # 실패율 담기
      f_rate.append(0 if c_num == 0 else s_num / c_num)
      answer.append(n)

      # 실패율을 정렬하여 스테이지 번호 담기
      for i in range(len(f_rate)-1,-1,-1):
        if i != 0:
          if f_rate[i] > f_rate[i-1]:
            f_rate[i], f_rate[i-1] = f_rate[i-1], f_rate[i]
            answer[i], answer[i-1] = answer[i-1], answer[i]

    return answer

N = 9
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4,4,4,4,4]
solution(N, stages)
