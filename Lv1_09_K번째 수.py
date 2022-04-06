# K번째 수

def solution(array, commands):
    answer = []
    for s, f, i in commands:
      temp_list = array[s-1:f]
      temp_list.sort()
      answer.append(temp_list[i-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)
