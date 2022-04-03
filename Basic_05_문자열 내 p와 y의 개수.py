# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    
    # y의 개수와 p의 개수
    cntY = s.count('Y') + s.count('y')
    cntP = s.count('P') + s.count('p')
    
    if cntY != cntP:
        answer = False

    return answer

s = "pPoooyY"
solution(s)
