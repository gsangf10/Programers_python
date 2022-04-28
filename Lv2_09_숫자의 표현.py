# 숫자의 표현

def solution(n):
    cnt = 0
    st_n = 1
    while True:
      s = 0
      for i in range(st_n,n+1):
        s += i
        if s < n:
          pass
        # 합이 n 보다 커지는 순간 검증 종료
        elif s > n:
          break
        # 합이 n을 만족하면 count 증가
        else:
          cnt += 1
      
      # 검증 시작 숫자가 n 이면 반복 종료
      if st_n == n:
        break

      # 시작 숫자 증가
      st_n += 1
      
    return cnt

n = 15
solution(n)
