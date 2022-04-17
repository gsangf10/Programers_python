# 양궁대회

r_info = []

# 가장 큰 점수부터 n발을 맞힐 경우를 구하는 재귀 함수
def ar_target(idx, arr, n):
  if sum(arr) == n:
    return r_info.append(arr)
  
  for i in range(idx, 11):
    arr[i] += 1
    ar_target(i, arr.copy(), n)
    arr[i] -= 1

# 각 사람의 점수를 구하는 함수
def get_score(a_list, r_list):
  a_score, r_score = 0, 0
  for i in range(len(r_list)):
    if r_list[i] != 0 or a_list[i] != 0:
      if r_list[i] > a_list[i]:
        r_score += 10 - i
      else:
        a_score += 10 - i

  return a_score, r_score
    

def solution(n, info):
    answer = []
    
    # 라이언이 쏴서 맞힐 모든 경우의 과녁
    ar_target(0, [0]*11, n)

    dif_dict = {}
    d_idx = []
    for i in range(len(r_info)):
      # 두 사람의 점수
      a_score, r_score = get_score(info, r_info[i])
      # 라이언이 가장 큰 점수로 이길 수 있는 인덱스 반환
      if r_score - a_score > 0:
        if r_score - a_score in dif_dict:
          dif_dict[r_score - a_score] += [i]
        else:
          dif_dict[r_score - a_score] = [i]
    
    # 딕셔너리 내림차순으로 튜플로 변형 후 정렬
    dif_tup = sorted(dif_dict.items(), reverse=True)
    
    # 두 사람이 무승부거나 라이언이 이길 수 없으면 -1 리턴
    # 점수 차가 있으면 해당 배열을 리턴
    if len(dif_tup) == 0:
      answer = [-1]
    else:
      best_idx = dif_tup[0][1]
      # 과녁 크기만큼 검사
      for i in range(10, -1, -1):
        # 최고 점수 차이인 인덱스로 검사
        for j in best_idx:
          # 저점으로 맞춘 경우가 있으면 저점을 많이 맞춘 배열을 처리
          if r_info[j][i] != 0:
            answer = r_info[j]
        # 저점이 나왔으면 체크 종료
        if len(answer) != 0:
          break
      
    return answer
    
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
solution(n, info)
