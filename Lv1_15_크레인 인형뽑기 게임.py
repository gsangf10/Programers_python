# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    cart = []

    for s_num in moves:
      s_num -= 1
      # 크레인이 인형을 만나면 바구니로 이동
      for x in range(len(board)):
        if board[x][s_num] != 0:
          cart.append(board[x][s_num])
          board[x][s_num] = 0
          break
      
      # 바구니에 같은 인형이 2개 연속할 경우 해당 인형 제거
      for i in range(len(cart)):
        if i != 0 and cart[i] == cart[i-1]:
          del cart[i-1:i+1]
          # 제거한 인형 count
          answer += 2
      
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)
