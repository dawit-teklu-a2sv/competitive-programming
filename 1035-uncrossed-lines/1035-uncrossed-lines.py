
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                
                if nums1[i] == nums2[j]:
                    print(i+1,j+1)
                    dp[i+1][j+1] =  1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
        return dp[len(nums1)][len(nums2)]
        
        memo = {}
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                memo[(i,j)] = 1 + solve(i+1,j+1)
            else:
                memo[(i,j)] = max(solve(i,j+1),solve(i+1,j))
            return memo[(i,j)]
        return solve(0,0)
            
        
        
        
        
        
        
        
        