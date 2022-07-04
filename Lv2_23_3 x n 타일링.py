# 3 x n 타일링
# 규칙 : 2 -> 3, 4 - -> 11, 6 -> 41, 8 -> 153, 10 -> 571, 12 -> 2131

def solution(n):
    n = n//2+1
    dp = [1,3] + [0 for i in range(2,n)]
    for i in range(2,n):
      dp[i] = dp[i-1] * 4 - dp[i-2]
    
    return dp[-1] % 1000000007

n = 12
solution(n)
