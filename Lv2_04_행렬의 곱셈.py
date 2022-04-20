# 행렬의 곱셈

def solution(arr1, arr2):
    m_list = []

    # 곱샘 결과 배열의 행
    for m in range(len(arr1)):
      m_list += [[]]
      # 곱샘 결과 배열의 열
      for n in range(len(arr2[0])):
        s = 0
        m_list[m] += [0]
        # 곱해서 더하는 횟수
        for k in range(len(arr2)):
          m_list[m][n] += arr1[m][k] * arr2[k][n]
        
    return m_list

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
solution(arr1, arr2)
