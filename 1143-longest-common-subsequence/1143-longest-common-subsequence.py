class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
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
        