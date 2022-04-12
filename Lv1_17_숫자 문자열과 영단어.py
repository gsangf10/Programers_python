# 숫자 문자열과 영단어

def solution(s):
    answer = 0
    en_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    s_list = list(s)
    
    # 영단어 검사 후 첫 자리는 숫자로 치환, 나머지 자리는 공백으로 치환
    for en in en_list:
      en_len = len(en)
      for i in range(len(s_list)):
        if s[i:i+en_len] == en:
          s_list[i] = str(en_list.index(en))
          k = 0
          for j in range(en_len-1):
            k += 1
            s_list[i+k] = ''

    answer = int(''.join(s_list))

    return answer

tc = "zeroone4seveneight"
solution(tc)
