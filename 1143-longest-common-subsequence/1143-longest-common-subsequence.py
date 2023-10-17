class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(text1) or j == len(text2):
                return 0 
            
            elif text1[i] == text2[j]:
                dp[(i,j)]  = 1 + solve(i+1,j+1)
            else:
                dp[(i,j)] = max(solve(i,j+1),solve(i+1,j))
            return dp[(i,j)]
        dp = {}
        return solve(0,0)
        