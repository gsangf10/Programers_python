# 쿼드압축 후 개수 세기

def is_only_num(a_list, num):
  is_only = False
  # 0 과 1 처리
  if num == 0:
    num = 1
  else:
    num = 0
  # 배열 구성이 한 숫자로만 되어있는지 검사
  for a in a_list:
    if num not in a:
      is_only = True
    else:
      is_only = False
    if is_only == False:
      return False
  return True

def quad_tree(a_list):
  global zero, one
  # 배열이 한 숫자로만 구성 되어있는지 검사
  if is_only_num(a_list, 0):
    zero += 1
    return True
  elif is_only_num(a_list, 1):
    one += 1
    return True
  else:
    # 4 등분으로 나누어 재귀 호출
    a_len = len(a_list)
    idx = a_len // 2
    st_idx, fn_idx = 0, idx
    for c in range(2):
      fst_list, scd_list = [], []
      for i in range(st_idx, fn_idx):
        fst_list.append(a_list[i][:idx])
        scd_list.append(a_list[i][idx:])
      st_idx, fn_idx = fn_idx, a_len
      # 재귀 호출
      quad_tree(fst_list)
      quad_tree(scd_list)

  return False

def solution(arr):
  global zero, one
  zero, one = 0, 0
  cnt = [0,0]
  quad_tree(arr)
  cnt[0] += zero
  cnt[1] += one
  return cnt

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# arr = [[1,1],[1,1]]
# arr = [[0,0],[0,0]]
# arr = [[0,1],[1,0]]
solution(arr)
