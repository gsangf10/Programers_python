#  예산

def solution(d, budget):
    answer = 0
    sum_d = 0

    # 부서별 신청한 예산을 오름차순으로 정력
    d.sort()

    # 신청 예산이 낮은순으로 더했을 때 총 예산을 넘지 않을 때 까지 지급
    for i in d:
      if sum_d + i > budget:
        break

      sum_d += i
      answer += 1

    return answer

d = [1,3,2,5,4]
budget = 9
solution(d, budget)
