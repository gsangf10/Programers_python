# 다음 큰 숫자

# 이진법 변환 함수
def conversion(n):
  s = 0
  for i in range(100,-1,-1):
    x = 2 ** i
    if n // x == 0:
      continue
    s += (n // x) * (10 ** i)
    n -= (n // x) * x
  return str(s)

# 이진법의 마지막부터 1의 갯수만큼 채우는 함수
def push_one(b_list, st_idx):
  one_cnt = b_list[st_idx:].count('1')
  re_len = len(b_list[st_idx:])
  update_zero = 0
  for j in range(re_len):
    if update_zero == re_len - one_cnt:
      b_list[st_idx+j] = '1'
    else:
      b_list[st_idx+j] = '0'
      update_zero += 1
  return b_list

def solution(n):
    b_num = list(conversion(n))

    b_len = len(b_num)

    zero_cnt = b_num.count('0')

    # 이진법 구성이 1로만 되있을 경우
    # => 인덱스 1번에 0을 추가하여 자릿수 늘림
    if zero_cnt == 0:
      b_num.insert(1,'0')
    else:
      one_cnt = 0
      last_one_idx = 0
      for i in range(b_len-1,-1,-1):
        # 이진법의 수가 1인 경우
        if b_num[i] == '1':
          one_cnt += 1

          # 1이 두번째인 경우
          if one_cnt == 2:
            between_zero_cnt = b_num[i:last_one_idx].count('0')

            # 마지막 1 사이에 0이 있는 경우
            # => 뒤의 1을 앞의 0이랑 자리바꿈
            if between_zero_cnt != 0:
              zero_idx = len(b_num[:last_one_idx]) - b_num[last_one_idx::-1].index('0')
              b_num[zero_idx], b_num[zero_idx+1] = '1', '0'
              
            else:
              front_zero_cnt = b_num[:i].count('0')
              
              # 앞부분에 0이 없는 경우
              if front_zero_cnt == 0:
                # 인덱스 1번에 0 추가하여 자릿수 늘림
                b_num.insert(1,'0')

                push_one(b_num, 1)

              # 앞부분에 0이 있는 경우
              # => 마지막 0과 뒤의 1을 자리바꿈
              else:
                last_zero_idx = len(b_num[:i]) - b_num[i::-1].index('0')
                b_num[last_zero_idx], b_num[last_zero_idx+1] = '1', '0'

                push_one(b_num, i)
          
          last_one_idx = i
                  
          # 검사 종료
          if one_cnt == 2:
            break

    answer = int(''.join(b_num), 2)
    
    return answer

n = 9999999
n = 78
solution(n)
