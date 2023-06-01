class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom-up
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        
        for i in range(2,n):
            dp[i] = max(dp[i-1],nums[i] + dp[i-2])
        
        return dp[n-1]
        
        #top-bottom
#         n = len(nums)
#         memo = {}
        
#         def solve(i):
#             if i == 0:
#                 return nums[0]
#             if i == 1:
#                 return max(nums[0],nums[1])
            
#             if i not in memo:
#                 memo[i] = max(solve(i-1),nums[i] + solve(i-2))
#             return memo[i]
#         return solve(n-1)
                
        