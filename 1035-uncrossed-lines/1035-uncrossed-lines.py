
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
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
            
        
        
        
        
        
        
        
        