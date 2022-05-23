# 가장 큰 정사각형 찾기

def solution(board):
    h_len = len(board) # 세로 길이
    w_len = len(board[0]) # 가로 길이

    # dp 준비
    dp = [[0]*w_len for _ in range(h_len)]
    dp[0] = board[0]
    for i in range(1,h_len):
      dp[i][0] = board[i][0]
    
    # 2중 포문으로 연산
    for i in range(1, h_len):
      for j in range(1, w_len):
        if board[i][j] == 1:
          dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # 최대 넓이 구하기
    square_len = 0
    for i in range(h_len):
      temp = max(dp[i])
      square_len = max(square_len, temp)
    
    return square_len**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,0,1,1,1],[1,1,0,0,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1]]
solution(board)
