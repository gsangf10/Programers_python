# 파괴되지 않은 건물

def solution(board, skill):
    cnt = 0
    n = len(board)
    m = len(board[0])

    # 누적합을 위한 초기값 설정
    b = [[0 for _ in range(m)] for _ in range(n)]

    for s in skill:
        b[s[1]][s[2]] += -s[5] if s[0] == 1 else s[5]
        if s[4] != m-1:
            b[s[1]][s[4]+1] += s[5] if s[0] == 1 else -s[5]
        if s[3] != n-1:
            b[s[3]+1][s[2]] += s[5] if s[0] == 1 else -s[5]
        if s[3] != n-1 and s[4] != m-1:
            b[s[3]+1][s[4]+1] += -s[5] if s[0] == 1 else s[5]

    # 누적합    
    for i in range(n):
        for j in range(m):
            if i == 0 and j != 0:
                b[i][j] += b[i][j-1]
            if i != 0 and j == 0:
                b[i][j] += b[i-1][j]
            if i != 0 and j != 0:
                b[i][j] += b[i-1][j] + b[i][j-1] - b[i-1][j-1]
        
    # board에 변화값 주기
    for i in range(n):
        board[i] = [a+b for a,b in zip(board[i], b[i])]
    
    # 내구도 1 이상인 건물의 수
    for i in range(n):
        tg = list(filter(lambda x : x > 0, board[i]))
        cnt += len(tg)

    return cnt

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
solution(board, skill)
