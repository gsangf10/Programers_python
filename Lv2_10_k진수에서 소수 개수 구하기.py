# k진수에서 소수 개수 구하기

# 진법 변환 함수
def conversion(n, k):
  s = 0
  for i in range(100,-1,-1):
    x = k ** i
    if n // x == 0:
      continue
    s += (n // x) * (10 ** i)
    n -= (n // x) * x
  return str(s)

# 소수 판별 함수
def is_prime(n):
  # 입력 값이 0이거나 1이면 Fasle
  if n == 0 or n == 1:
    return False
  # 2이면 True
  elif n == 2:
    return True
  # 짝수이면 False
  elif n % 2 == 0:
    return False
  d_cnt = 0
  # 99 까지만 검사
  for i in range(3,100,2):
    # 나누어 떨어지면
    if n % i == 0:
      # 나누어 떨어지는 수가 n 이면 True
      if n == i:
        return True
      else:
        d_cnt = 1
        break
  if d_cnt == 0:
    return True

  return False

def solution(n, k):
    d_num = conversion(n, k)
    cnt = 0
    s = '0'
    for i in range(len(d_num)):
      if d_num[i] == '0' or i == len(d_num)-1:
        # 진법의 마지막 수일 경우 해당 숫자 넣기
        if i == len(d_num)-1:
          s += d_num[i]
        # 소수인지 판별
        if is_prime(int(s)):
          cnt += 1
        # 문자열 초기화
        s = '0'
      else:
        s += d_num[i]

    return cnt

n = 437674
# n = 110011
n = 1000000
k = 3
# k = 10
solution(n, k)
