class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        
        def solve(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            
            if i not in memo:
                memo[i] = max(solve(i-1),nums[i] + solve(i-2))
            return memo[i]
        return solve(n-1)
                
        