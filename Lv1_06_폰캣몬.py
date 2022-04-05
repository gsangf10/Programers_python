# 폰캣몬

def solution(nums):
    answer = 0

    # 가져갈 수 있는 폰켓몬 수
    t_num = len(nums) // 2

    # 폰켓몬의 종류
    t_cnt = len(set(nums))

    # 폰켓몬의 종류가 가져갈 수 있는 수보다 크면 각각 다른 종류를 가져갈 수 있다.
    if t_cnt >= t_num:
      answer = t_num
    else:
      answer = t_cnt

    return answer

nums = [3,3,3,2,2,4]
solution(nums)
