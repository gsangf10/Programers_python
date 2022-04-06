# 완주하지 못한 선수

# 이 함수는 효율성 검사에서 fail
# def solution(participant, completion):
#     answer = ''
    
#     # 완주한 선수들은 선수 명단에서 제거
#     for c in completion:
#       participant.remove(c)

#     answer = participant[0]

#     return answer


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    # 완주한 선수들은 선수 명단에서 제거
    for i in range(len(completion)):
      if participant[i] != completion[i]:
        answer = participant[i]
        break
      elif i == len(completion)-1:
        answer = participant[-1]

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)
