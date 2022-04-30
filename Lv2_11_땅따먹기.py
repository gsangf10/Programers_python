# 땅따먹기

def solution(land):
    answer = 0
    n = len(land)

    for i in range(1, n):
      # 해당 부분에 이전 배열의 가장 높은 수를 더하기
      land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
      land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
      land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
      land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    # 마지막 배열의 가장 큰 수 반환
    answer = max(land[n-1])

    return answer
  
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
solution(land)
