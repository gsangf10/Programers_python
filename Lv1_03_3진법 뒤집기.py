# 3진법 뒤집기

def solution(n):
    answer = 0
    t_num = []

    # 3진법 자릿수 구하기
    k = 1
    while True:
      if 3 ** k > n:
        break
      k += 1
    
    # 3진법으로 변환
    for i in range(k-1,-1,-1):
      v_num = n//(3**i)
      t_num += [v_num]
      n -= (3**i) * v_num

    # 뒤집기
    t_num.reverse()
    
    # 10진법으로 변환
    k = 0
    for i in range(len(t_num)-1,-1,-1):
      answer += t_num[i] * (3**k)
      k += 1

    return answer

n = 45
solution(n)
