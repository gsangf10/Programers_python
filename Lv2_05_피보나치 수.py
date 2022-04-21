# 피보나치 수

def fibo_num(n):
  # 기본 조건
  if n == 1 or n == 2:
    return 1

  # 입력 받은 수 만큼 빈 배열 생성
  f_list = [0 for i in range(n+1)]
  # 기본 조건 삽입
  f_list[1], f_list[2] = 1, 1

  # 인덱스 3번부터 이전 두 인덱스의 배열을 더하기
  for i in range(3,n+1):
    f_list[i] = f_list[i-1] + f_list[i-2]

  # 마지막 인덱스 리턴
  return f_list[-1]

def solution(n):
    # 피보나치 수를 구해 1234567 로 나눈 나머지 리턴
    return fibo_num(n) % 1234567

n = 5
solution(n)
