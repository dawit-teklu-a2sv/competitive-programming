class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[-1][-1] = 1
        
        def answerOrDefault(r,c):
            if 0 <= r < m and 0 <= c < n:
                return dp[r][c]
            else:
                return 0
            
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                dp[row][col] = dp[row][col] + answerOrDefault(row+1,col) + answerOrDefault(row,col + 1)
        return dp[0][0]
        