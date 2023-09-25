class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def solve(i,j,text1,text2):
            if i < 0 or j < 0:
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            elif text1[i] == text2[j]:
                dp[i][j] = 1 + solve(i-1,j-1,text1,text2)
            else:
                dp[i][j] = max(solve(i-1,j,text1,text2),solve(i,j-1,text1,text2))
            return dp[i][j]
        
        n = len(s) - 1
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return solve(n,n,s,s[::-1])
        