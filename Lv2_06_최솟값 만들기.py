# 최솟값 만들기

def solution(list_A,list_B):
    # A 리스트와 B 리스트 정렬
    list_A.sort()
    list_B.sort(reverse=True)
    sum = 0
    # 각 항의 순대로 곱해서 더하기
    for i in range(len(list_A)):
      sum += list_A[i] * list_B[i]

    return sum

list_A = [1, 4, 2]
list_B = [5, 4, 4]	
solution(list_A,list_B)
