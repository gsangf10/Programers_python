# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0

    for n in range(left,right+1):
      # 약수의 개수 구하기
      d_cnt = 0
      for i in range(1,n+1):
        if n % i == 0:
          d_cnt += 1

      # 약수의 수가 짝수이면 더하기, 홀수이면 빼기
      if d_cnt % 2 == 0:
        answer += n
      else:
        answer -= n

    return answer

left = 13
right = 17
solution(left, right)
