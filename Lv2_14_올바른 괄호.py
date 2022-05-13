# 올바른 괄호

def solution(s):
    # 처음 시작이 닫는 괄호 ')' 이면 False
    if s[0] == ')':
      return False
    # 마지막이 여는 괄호 '(' 이면 False
    elif s[-1] == '(':
      return False
    else:
      # '('와 ')'의 갯수 구하기
      open_cnt = 0
      close_cnt = 0
      for i in range(len(s)):
        if s[i] == '(':
          open_cnt += 1
        else:
          close_cnt += 1
        # 검사 중 '(' 보다 ')'의 수가 커지면 False
        if open_cnt < close_cnt:
          return False
      # '('와 ')'의 수가 같지 않으면 False
      if open_cnt != close_cnt:
        return False
    return True

s = "(()))(()"
solution(s)
