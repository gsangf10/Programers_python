# [3차] 파일명 정렬

def is_str_big(str1, str2):
  b_alpha = [chr(i) for i in range(65,91)]
  str1_len = len(str1)
  str2_len = len(str2)
  for q in range(str1_len):
    if q == str2_len:
      return True
    # 공백 체크
    if str1[q] == ' ' and str2[q] == ' ':
      continue
    elif str1[q] == ' ' and str2[q] != ' ':
      return False
    elif str1[q] != ' ' and str2[q] == ' ':
      return True
    # 특수문자 비교
    if str1[q] not in b_alpha and str2[q] not in b_alpha:
      if ord(str1[q]) < ord(str2[q]):
        return False
      elif ord(str1[q]) > ord(str2[q]):
        return True
      else:
        continue
    elif str1[q] in b_alpha and str2[q] not in b_alpha:
      return False
    elif str1[q] not in b_alpha and str2[q] in b_alpha:
      return True
    # 문자 비교
    if ord(str1[q]) < ord(str2[q]):
      return False
    elif ord(str1[q]) > ord(str2[q]):
      return True
  return False


def solution(files):
    num_list = [str(i) for i in range(0,10)]

    f_order = files
    f_cnt = len(files)

    # 파일명을 머리, 숫자, 꼬리로 나누기
    f_list = []
    for idx, f_name in enumerate(files):
      f_head = ''
      f_num = ''
      f_tail = ''
      for i in range(len(f_name)):
        if f_name[i] not in num_list and f_name[i-1] in num_list and f_head != '':
          f_tail = f_name[i:]
          break
        else:
          if f_name[i] in num_list:
            f_num += f_name[i]
          else:
            f_head += f_name[i]

      f_list.append({'f_head':f_head,'f_num':f_num,'f_tail':f_tail})
    
    # 버블정렬
    for i in range(f_cnt-1,-1,-1):
      for j in range(0,i):
        current_h = f_list[j]['f_head'].upper()
        next_h = f_list[j+1]['f_head'].upper()
        # head 부분 기준으로 정렬
        if current_h != next_h:
          # 현재 head 부분이 다음 head 보다 큰지 검사
          is_big = is_str_big(current_h,next_h)
          if is_big:
            f_list[j], f_list[j+1] = f_list[j+1], f_list[j]
            f_order[j], f_order[j+1] = f_order[j+1], f_order[j]
          continue
        
        # 숫자부분에 따른 정렬
        current_n = 0
        next_n = 0
        if f_list[j]['f_num'] != '' and f_list[j+1]['f_num'] != '':
          current_n = int(f_list[j]['f_num'])
          next_n = int(f_list[j+1]['f_num'])
        if current_n > next_n:
          f_list[j], f_list[j+1] = f_list[j+1], f_list[j]
          f_order[j], f_order[j+1] = f_order[j+1], f_order[j]

    return f_order

files = ["img12.png", "img10.png", "img02.png", "foo.as.d122.zip", "foo-a-s.d122.zip", "img1.png", "foo.a-s.d122.zip", "IMG01.GIF", "img2.JPG", "f--.g15", "f..-.g15", "F.-g15", "f-.g15", "emon01.txt", "Fg-f15", "F .f17", "F -f15", "F-f15", "F-g15", "f15", "f1"]
solution(files)
