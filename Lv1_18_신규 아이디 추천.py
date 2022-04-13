# 신규 아이디 추천

def solution(new_id):
    answer = ''

    # 1단계 : 대문자를 소문자로 치환
    answer = new_id.lower()

    # 2단계 : 소문자, 숫자, -, _, . 를 제외한 문자 제거
    id_list = list(answer)
    for i, c in enumerate(id_list):
      # 문자를 아스키코드로 변환하여 검사
      if ord(c) == 45 or ord(c) == 46 or ord(c) == 95:
        continue
      elif ord(c) >= 48 and ord(c) <= 57:
        continue
      elif ord(c) >= 97 and ord(c) <= 122:
        continue
      else:
        id_list[i] = ''

    answer = ''.join(id_list)

    # 3단계 : 마침표가 2번 이상 연속된 부분 제거
    id_list = list(answer)
    for i in range(len(id_list)-1):
      if id_list[i] == '.' and id_list[i+1] == '.':
        id_list[i] = ''
        
    answer = ''.join(id_list)

    # 4단계 : 마침표가 처음이나 마지막에 있다면 마침표 제거
    if len(id_list) != 0:
      id_list = list(answer)
      if id_list[0] == '.':
        id_list[0] = ''
      if id_list[-1] == '.':
        id_list[-1] = ''
        
      answer = ''.join(id_list)

    # 5단계 : 빈 문자열이라면 'a'를 대입
    if answer == '':
      answer = 'a'

    # 6단계 : 길이가 16자 이상이면 15자까지를 제외한 나머지 문자 제거
    # 만약 문자 제거 후 마침표가 마지막에 위치 하면 마침표 제거
    if len(answer) > 15:
      answer = answer[:15]
      if answer[-1] == '.':
        answer = answer[:14]

    # 7단계 : 길이가 2자 이하면 마지막 문자를 길이가 3이 될 때까지 반복 삽입
    for i in range(2):
      if len(answer) < 3:
        answer += answer[-1]
    
    return answer

# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
# new_id = "abcdefghijklmn.p"
# new_id = "a...a"
new_id = "/..D.SNA....IDNSAI....N,.,..D1,,...Q21.....41@...@_@#$(@_!$(*$!(#@,...21.."
solution(new_id)
