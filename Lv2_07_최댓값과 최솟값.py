# 최댓값과 최솟값

def solution(s):
    answer = ''
    # 문자열을 리스트로 변환
    s_list = list(map(int,s.split()))
    # 리스트를 오름차순으로 정렬 : 처음이 최솟값, 마지막이 최댓값
    s_list.sort()
    # 최솟값과 최댓값 출력
    answer += str(s_list[0]) + ' ' + str(s_list[-1])

    return answer

s = "1 2 3 4"
solution(s)
