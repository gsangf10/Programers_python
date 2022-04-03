# 콜라츠 추측

def solution(num):
    answer = 0
    # 1이 아닐 때 까지 반복
    while num != 1:
        # 짝수라면 나누기 2, 홀수라면 3 곱하고 더하기 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        # 반복 횟수 증가
        answer += 1
        # 500번 반복해도 1이 되지 않으면 -1 리턴
        if answer == 500 and num != 1:
            answer = -1
            break;
    return answer

num = 6
solution(num)
