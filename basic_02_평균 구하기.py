# 평균 구하기

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer /= len(arr)
    return answer

arr = [1,2,3,4]
solution(arr)
