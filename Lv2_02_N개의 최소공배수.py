# N개의 최소공배수

def solution(arr):
    answer = 0
    
    # 배열을 내림차순으로 정렬
    arr.sort(reverse=True)

    # 100개씩 검사
    st_n = 1
    fs_n = 101
    while True:
      # 정답을 찾았으면 검사 종료
      if answer != 0:
        break

      # 배열 중 가장 큰 수의 배수 집합
      mtp_list = [arr[0]*i for i in range(st_n,fs_n)]
      bool_chk = [False]*len(arr)

      # 가장 큰 수의 배수 집합에서 모든 수가 약수로 들어가는 배수 검사
      for m in mtp_list:
        for i in range(len(arr)):
          if m % arr[i] == 0:
            bool_chk[i] = True
          else:
            bool_chk[i] = False
        # 모든 배열이 약수집합이 되면 검사 종료
        if bool_chk.count(False) == 0:
          answer = m
          break
      
      # 다음 검사 조건 설정
      st_n += 100
      fs_n += 100
    
    return answer

arr = [2,6,8,14]
solution(arr)
