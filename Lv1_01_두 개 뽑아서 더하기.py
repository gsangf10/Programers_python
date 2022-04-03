# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []

    # 배열 중 두개를 뽑아 더해서 저장
    for x in range(len(numbers)):
      for y in range(x+1, len(numbers)):
        answer += [numbers[x] + numbers[y]]

    # 저장된 배열을 중복제거 하여 다시 정렬
    answer = list(set(answer))
    answer.sort()

    return answer

numbers = [2,1,3,4,1]
solution(numbers)
