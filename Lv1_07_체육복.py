# 체육복

def solution(n, lost, reserve):
    answer = 0
    s_cnt = [1 for i in range(n)]
    
    # 체육복 있는 학생 -> 1, 체육복 없는 학생 -> 0
    for l in lost:
      s_cnt[l-1] = 0
      # 여벌 체육복이 있는 학생중 도난당한 학생 검사
      if reserve.count(l) != 0:
        reserve.remove(l)
        s_cnt[l-1] = 1

    for i in range(n):
      # 체육복이 없는 사람
      if s_cnt[i] == 0:
        # 앞 번호가 여벌이 있는지 검사
        if i != 0 and reserve.count(i) != 0:
          reserve.remove(i)
          s_cnt[i] = 1
        # 뒷 번호가 여별이 있는지 검사
        elif i != n-1 and reserve.count(i+2) != 0:
          reserve.remove(i+2)
          s_cnt[i] = 1
    
    # 체육 수업에 나갈 수 있는 학생 수
    for i in s_cnt:
      answer += i
    
    return answer

n = 5
lost = [2, 4]
reserve =[1, 3, 5]
solution(n, lost, reserve)
