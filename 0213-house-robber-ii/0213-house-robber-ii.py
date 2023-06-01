class Solution:
    def rob(self, nums: List[int]) -> int:

        
        def solve(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0],dp[1] = nums[0],max(nums[0],nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1],nums[i] + dp[i-2])

            return dp[n-1]    
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = solve(nums[:n-1])
        ans2 = solve(nums[1:])
        return max(ans1,ans2)
        