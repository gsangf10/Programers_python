# 음양 더하기

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
      sign = 1
      # 매개변수 값이 False이면 음수
      if signs[i] == False:
        sign = -1
          
      answer += absolutes[i] * sign

    return answer

absolutes = [4,7,12]
signs = [True,False,True]
solution(absolutes, signs)
