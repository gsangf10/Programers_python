# 소수 만들기

def solution(nums):
    answer = 0
    
    # 순차적으로 3개 숫자 배열에 담기
    for x in range(len(nums)-1, 1, -1):
      for y in range(x-1, 0, -1):
        for z in range(y-1, -1, -1):
          # 배열 중복삽입 체크
          if x == y or x == z or y == z:
            continue
          
          # 배열에 3개 숫자 담기
          n_list = []
          n_list.append(nums[x])
          n_list.append(nums[y])
          n_list.append(nums[z])

          # 3개 숫자의 합
          n_sum = 0
          for i in range(3):
            n_sum += n_list[i]
          
          # 약수의 합
          d_sum = 0
          for i in range(1,n_sum+1):
            if n_sum % i == 0:
              d_sum += i
          
          # 3개 숫자의 합이 소수인지 검사
          if d_sum == n_sum+1:
            answer += 1

    return answer

nums = [1,2,7,6,4]
# nums = [1,2,3,4]
solution(nums)
