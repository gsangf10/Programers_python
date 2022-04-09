# 없는 숫자 더하기

def solution(numbers):
    answer = 0

    # 매개변수 정렬
    numbers.sort()

    # 0 ~ 9 중 존재하지 않는 숫자 찾아서 더하기
    for i in range(10):
      if numbers.count(i) == 0:
        answer += i

    return answer

# numbers = [1,2,3,4,6,7,8,0]
numbers = [5,8,4,0,6,7,9]
solution(numbers)
