# [3차] n진수 게임

n_list = [str(i) for i in range(10)] + ['A','B','C','D','E','F','X']

# 수가 진법에 맞게 증가하는 함수
def increase_digits(num, n):
  # 자릿수가 하나라면 앞에 1 추가후 종료
  if len(num) == 1:
    num.insert(0,'1')
    return num
  # 마지막 둘째 자리 증가
  num[-2] = n_list[n_list.index(num[-2])+1]
  # 마지막 둘째 자리부터 수가 진법에 맞는지 검사하여 자릿수 증가
  for i in range(len(num)-2,-1,-1):
    if num[i] == n_list[n]:
      # 첫째 자리라면 맨 앞에 1을 추가하고 종료
      if i == 0:
        num[i] = '0'
        num.insert(0,'1')
        break
      num[i] = '0'
      num[i-1] = n_list[n_list.index(num[i-1])+1]

  return num

def solution(n, t, m, p):
    answer = ''
    s_num = ['0']
    n_idx = 0

    player = ['']*m
    p_idx = 0

    while True:
      # 자릿수 증가
      if n_idx == n:
        increase_digits(s_num, n)
        n_idx = 0

      s_num[-1] = n_list[n_idx]
      n_idx += 1

      # 수를 체크하여 플레이어 순서대로 넣기
      for num in s_num:
        player[p_idx] = num
        # 본인 순서가 되면 해당 수를 저장
        if p_idx == p-1:
          answer += player[p_idx]
        # 순서가 총 인원을 넘어가게 되면 다시 처음 사람으로 돌아감
        if p_idx == m-1:
          p_idx = 0
        else:
          p_idx += 1

      if len(answer) >= t:
        break
    
    return answer[:t]

n = 2  # 진법
n = 16
t = 16  # 미리 구할 숫자의 갯수
m = 2  # 인원
p = 1  # 순서
solution(n, t, m, p)
