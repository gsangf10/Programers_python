# JadenCase 문자열 만들기

def solution(s):
    answer = ''

    for i in range(len(s)):
      # 가장 처음 나오는 문자는 대문자 처리
      if i != 0:
        # 전 문자가 공백이며면 대문자 처리하고 아니면 소문자 처리
        if s[i-1] == ' ':
          answer += s[i].upper()
        else:
          answer += s[i].lower()
      else:
        answer += s[i].upper()
    
    return answer

s = "3people unFollowed me"
solution(s)
