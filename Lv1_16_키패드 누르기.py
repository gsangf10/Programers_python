# 키패드 누르기

def solution(numbers, hand):
    answer = ''

    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    h_position = {"p_left" : [3, 0], "p_right" : [3, 2]}

    for num in numbers:
      for x in range(len(keypad)):
        for y in range(len(keypad[x])):
          # 키패드에서 해당 숫자 위치 찾기
          if keypad[x][y] == num:
            # 1, 4, 7 왼손 입력
            if num in (1, 4, 7):
              answer += "L"
              h_position["p_left"] = [x, y]
            # 3, 6, 9 오른손 입력
            elif num in (3, 6, 9):
              answer += "R"
              h_position["p_right"] = [x, y]
            else:
              l_posit = h_position["p_left"]
              r_posit = h_position["p_right"]
              r_dist, l_dist = 9, 9

              # 왼손 거리 계산 
              if x == l_posit[0] and y == l_posit[1]:
                l_dist = 0
              elif x == l_posit[0]:
                l_dist = 1
              elif y == l_posit[1]:
                l_dist = abs(x - l_posit[0])
              else:
                l_dist = abs(x - l_posit[0]) + 1

              # 오른손 거리 계산
              if x == r_posit[0] and y == r_posit[1]:
                r_dist = 0
              elif x == r_posit[0]:
                r_dist = 1
              elif y == r_posit[1]:
                r_dist = abs(x - r_posit[0])
              else:
                r_dist = abs(x - r_posit[0]) + 1

              # 거리가 같을 경우 왼손잡이의 경우 왼손, 오른손잡이의 경우 오른손
              if l_dist == r_dist:
                if hand == "right":
                  answer += "R"
                  h_position["p_right"] = [x, y]
                else:
                  answer += "L"
                  h_position["p_left"] = [x, y]
              # 오른손이 더 가까울 경우
              elif l_dist > r_dist:
                answer += "R"
                h_position["p_right"] = [x, y]
              # 왼손이 더 가까울 경우
              elif l_dist < r_dist:
                answer += "L"
                h_position["p_left"] = [x, y]

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers, hand)
